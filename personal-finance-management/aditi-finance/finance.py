import openpyxl
import io
import pandas as pd
from google.cloud import storage
from google.cloud import bigquery
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.api_core.exceptions import NotFound
import pyarrow
from datetime import datetime

folder_A_id = '1wOcHg0xO5ABV9pt_4RrHbPNNdWOZF-Hg'
target_bucket_name = 'aditi-finance-raw'
gcs_folder_name = 'finance'
gcs_file_name = 'file_list.txt'
project_id = "abhinav-dev"
bq_table_name = "bank-statements"
bq_dataset_name = "aditi_finance"

def get_object_names():
  file_contents = []
  client = storage.Client()
  bucket = client.bucket(target_bucket_name)
  blob_name = f"{gcs_folder_name}/{gcs_file_name}"
  blob = bucket.blob(blob_name)
  if not blob.exists():
    blob.upload_from_string('')
    return file_contents
  else:
    text_content = blob.download_as_text()
    gcs_list = text_content.split("\n")
    return gcs_list


def new_files_to_load(list1, list2):
    new_files = []
    list1_new = [x[:-5] for x in list1]
    print("list one", list1_new)
    list2_new = [x[:-4] for x in list2]
    print("list two", list2_new)
    for source_object in list1_new:
        if source_object in list2_new:
            continue
        else:
            new_files.append(f"{source_object}.xlsx")
    print("new files are: ", new_files)
    
    return new_files

def get_file_list():
    credentials, _ = google.auth.default(
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets.readonly", "https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.metadata.readonly"
    ]
    )
    try:
        # create drive api client
        service = build('drive', 'v3', credentials=credentials)
        files = []
        file_list = []
        page_token = None
        query = f"mimeType != 'application/vnd.google-apps.folder' and trashed = false and '{folder_A_id}' in parents and trashed = false"
        while True:
            response = service.files().list(q=query, spaces='drive', fields='nextPageToken, files(id, name)', pageToken=page_token).execute()
            for file in response.get('files', []):
                print(file.get("name"))
                file_list.append(file.get("name"))
            files.extend(response.get('files', []))
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break

    except HttpError as error:
        print(F'An error occurred: {error}')
        files = None

    return file_list

def xlsx_to_df(file_name):
    credentials, _ = google.auth.default(
        scopes=[
            "https://www.googleapis.com/auth/spreadsheets.readonly", "https://www.googleapis.com/auth/drive"
        ]
    )
    # Get the file URL
    drive_service = build('drive', 'v3', credentials=credentials)

    query = f"trashed = false and mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' and name='{file_name}' and '{folder_A_id}' in parents"
    results = drive_service.files().list(q=query, spaces='drive', fields='nextPageToken, files(id)').execute()
    items = results.get('files', [])
    
    file_id = items[0]['id']
    request = drive_service.files().get_media(fileId=file_id)

    # Read file data into dataframe
    file_content = io.BytesIO(request.execute())
    df = pd.read_excel(file_content)
    return df


def load_to_bq(df):
    # Read in the data from the file and process it
    df.columns = ['transaction_date', 'narration', 'ref_no', 'value_date', 'withdrawal_amt', 'deposit_amt', 'closing_balance']
    df['transaction_date'] = pd.to_datetime(df['transaction_date'], format='%d/%m/%y')
    df['value_date'] = pd.to_datetime(df['value_date'], format='%d/%m/%y')
    bq_client = bigquery.Client(project=project_id)
    dataset_ref = bq_client.dataset(bq_dataset_name)
    dataset = bigquery.Dataset(dataset_ref)
    dataset.location = "europe-west2"
    try:
        bq_client.get_dataset(dataset)
    except NotFound:
        # If the dataset does not exist, create it
        bq_client.create_dataset(dataset)
        
    table_path = f"{project_id}.{bq_dataset_name}.{bq_table_name}"
    try:
        table = bq_client.get_table(table_path)
        
        job_config = bigquery.LoadJobConfig()
        job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND
        job = bq_client.load_table_from_dataframe(df, table_path, job_config=job_config)
    
    except NotFound:
        # Table does not exist, create the table and load the data
        schema = [
            bigquery.SchemaField("transaction_date", "DATETIME"),
            bigquery.SchemaField("narration", "STRING"),
            bigquery.SchemaField("ref_no", "STRING"),
            bigquery.SchemaField("value_date", "DATETIME"),
            bigquery.SchemaField("withdrawal_amt", "FLOAT"),
            bigquery.SchemaField("deposit_amt", "FLOAT"),
            bigquery.SchemaField("closing_balance", "FLOAT")

        ]

        table = bigquery.Table(table_path, schema=schema)
        table = bq_client.create_table(table)
        job_config = bigquery.LoadJobConfig()
        job_config.schema = schema
        job = bq_client.load_table_from_dataframe(df, table_path, job_config=job_config)
        job.result()
    return df

def load_to_storage(file_name):
  client = storage.Client()
  bucket = client.bucket(target_bucket_name)
  blob_name = f"{gcs_folder_name}/{gcs_file_name}"
  blob = bucket.blob(blob_name)
  text_content = blob.download_as_text()
  text_content = text_content + "\n" + file_name
  blob.upload_from_string(text_content, content_type='text/plain')

def main():
    file_list = get_file_list()
    object_list = get_object_names()
    new_files = new_files_to_load(file_list, object_list)
    print("new files --->", new_files)
    for file_name in new_files:
        df = xlsx_to_df(file_name)
        df = load_to_bq(df)
        load_to_storage(file_name[:-5])
    return "ok"
main()


# gcp_helper.py

import gspread
import google.auth
from googleapiclient.discovery import build
from gspread.exceptions import SpreadsheetNotFound, APIError
from requests.exceptions import HTTPError
import random
from google.cloud import secretmanager

PROJECT_NO = 983346229653

def get_gsheet_credentials(google_sheet_name):
    credentials, _ = google.auth.default(
    scopes = [
                "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"
            ]
        )
    gspread_client = gspread.Client(auth=credentials)
    gsheet = gspread_client.open(google_sheet_name)
    return gsheet


def check_if_wsheet_present(google_sheet_name, sheet):
    try:
        gsheet = get_gsheet_credentials(google_sheet_name)
        worksheet = None
        for existing_worksheet in gsheet.worksheets():
            if existing_worksheet.title == sheet:
                worksheet = existing_worksheet
                return worksheet

        if worksheet is None:
            print(f"Worksheet '{sheet}' not found.")
            return None
    
    except SpreadsheetNotFound as e:
        print("Spreadsheet not found:", e)
    except APIError as e:
        print("API error occurred:", e)  
    except ConnectionError as e:
        print(f"Connection error occurred: {e}")

def create_worksheet(google_sheet_name, topic_name):
    gsheet = get_gsheet_credentials(google_sheet_name)
    worksheet = gsheet.add_worksheet(title=topic_name, rows="10000", cols="26")
    worksheet.append_row(["Topic Names"])

def write_in_gsheet(google_sheet_name, sheet, topics_list):
        
        result = check_if_wsheet_present(google_sheet_name, sheet)
        if result is not None:
            worksheet = result
        if result is None:
            create_worksheet(sheet)
            
        existing_terms = worksheet.col_values(1)
    
        new_terms = []
        for term in set(topics_list):
            if term not in existing_terms:
                new_terms.append([term])

        if new_terms:
            worksheet.append_rows(new_terms, value_input_option='USER_ENTERED')
                    


def sort_sheet(google_sheet_name, sheet):
    column_index = 0
    worksheet = check_if_wsheet_present(google_sheet_name, sheet)
    if (worksheet):
        values = worksheet.get_all_values()
        header = values[0]
        data_rows = values[1:]
        sorted_rows = sorted(data_rows, key=lambda x: x[column_index])
        sorted_values = [header] + sorted_rows
        worksheet.clear()
        worksheet.update("A1", sorted_values)           

def read_from_gsheet(INPUT_GSHEET_NAME, topic_name):
    worksheet_input = check_if_wsheet_present(INPUT_GSHEET_NAME, topic_name)
    if (worksheet_input):
        values = worksheet_input.get_all_values()
        header = values[0]
        data_rows = values[1:]
        random_term = random.choice(data_rows)
        return random_term
    else:
        print("No worksheet found")
        return False
    

def access_secret_version(secret_id, version_id=1):
    client = secretmanager.SecretManagerServiceClient()

    name = f"projects/{PROJECT_NO}/secrets/{secret_id}/versions/{version_id}"
    response = client.access_secret_version(name=name)

    return response.payload.data.decode("UTF-8")


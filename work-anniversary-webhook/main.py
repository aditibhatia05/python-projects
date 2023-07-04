from json import dumps
from httplib2 import Http
import gspread
import datetime
import google.auth
import json
import random
import requests
from google.cloud import secretmanager

SHEET_NAME = "work anniversaries"
PROJECT_NO = 123456789101
SPACE_ID = 'AABBadlT3t8'


gif_urls = [
    "https://media.giphy.com/media/TKpA0H608ywi0DWT0u/giphy.gif",
    "https://media.giphy.com/media/xvny8QpYmlur4qMVpy/giphy.gif",
    "https://media.giphy.com/media/h6XuKWAblJ85p6vb1X/giphy.gif",
    "https://media.giphy.com/media/xvny8QpYmlur4qMVpy/giphy.gif",
    "https://media.giphy.com/media/zWXtPswhdr1S4Dz5Rz/giphy.gif"

]

def get_ann_names():
    credentials, _ = google.auth.default(
        scopes=[
            "https://www.googleapis.com/auth/spreadsheets.readonly", "https://www.googleapis.com/auth/drive"
        ]
    )
    gspread_client = gspread.Client(auth=credentials)
    gsheet = gspread_client.open(SHEET_NAME)
    worksheet = gsheet.get_worksheet(0)
    date_column = worksheet.col_values(2)
    name_column =  worksheet.col_values(1)

    names_list=[]

    today = datetime.date.today()
    today_date = today.strftime('%d')
    today_month = today.strftime('%m')

    for i in range(1, len(date_column)):
        date_str = date_column[i]
        date_obj = datetime.datetime.strptime(date_str, '%d/%m/%Y')
        date = date_obj.date()
        month = date_obj.month
        if date.strftime('%d') == today.strftime('%d') and str(month).zfill(2) == today.strftime('%m'):
            names_list.append(name_column[i])
    
    return names_list

def access_secret_version(secret_id, version_id=1):
    client = secretmanager.SecretManagerServiceClient()

    name = f"projects/{PROJECT_NO}/secrets/{secret_id}/versions/{version_id}"
    response = client.access_secret_version(name=name)

    return response.payload.data.decode("UTF-8")

def main(request):
    names = get_ann_names()
    print(names)
    random_gif_url = random.choice(gif_urls)
    api_key = access_secret_version("webhook-api-key")
    token = access_secret_version("webhook-token")
    text_message = f"Happy Work anniversary! {', '.join(names)}"
    webhook_url = f"https://chat.googleapis.com/v1/spaces/SPACE_ID/messages?key={api_key}&token={token}"
    bot_message = {
    "text": text_message,
    "cards": [
            {
            "sections": [
                    {
                    "widgets": [
                            {
                            "image": {
                                "imageUrl": random_gif_url
                                }
                            }
                        ]
                    }
                ]
            }   
        ]
    }
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()
    response = http_obj.request(
        uri=webhook_url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )
    print(response)

    return "Successful"

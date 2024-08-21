import requests
import os

def run(event, context):
    url = "https://notify-api.line.me/api/notify"
    access_token = os.environ['LINE_NOTIFY_CLIENT_TOKEN']
    headers = {'Authorization': 'Bearer ' + access_token}
    message = 'お掃除当番表テスト'
    payload = {'message': message}
    r = requests.post(url, headers=headers, params=payload,)


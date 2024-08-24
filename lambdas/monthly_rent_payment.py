import requests
import os

def run(event, context):
    url = "https://notify-api.line.me/api/notify"
    access_token = os.environ['LINE_NOTIFY_CLIENT_TOKEN']
    headers = {'Authorization': 'Bearer ' + access_token}
    message = '明日25日は家賃の支払日です。忘れないうちに家賃を払いましょう。'
    payload = {'message': message }
    r = requests.post(url, headers=headers, params=payload,)

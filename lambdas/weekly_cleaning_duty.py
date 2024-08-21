import requests
import os
from datetime import datetime

def run(event, context):
    url = "https://notify-api.line.me/api/notify"
    access_token = os.environ['LINE_NOTIFY_CLIENT_TOKEN']
    headers = {'Authorization': 'Bearer ' + access_token}
    message = get_cleaner_list(get_week_number(event['time']))
    payload = {'message': message}
    r = requests.post(url, headers=headers, params=payload,)

def get_week_number(datetime_str):
    # Convert the string to a datetime object
    date_obj = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%SZ")

    # Get the week number
    week_number = date_obj.isocalendar().week

    return week_number

def get_cleaner_list(week_number):
    residents = ['かえで', '鈴木', 'ななこ', '恒河', 'SJ']
    cleaning_tasks = ['トイレ＆シャワー', '洗面所＆キッチン', '床掃除', '共用のタオル', 'ゴミ捨て']

    # Calculate the starting index based on the week number
    start_index = week_number % len(residents)

    # Rotate the list of residents based on the starting index
    rotated_residents = residents[start_index:] + residents[:start_index]

    # Create the message string
    message_lines = [f"①{cleaning_tasks[0]}：{rotated_residents[0]}",
                     f"②{cleaning_tasks[1]}：{rotated_residents[1]}",
                     f"③{cleaning_tasks[2]}：{rotated_residents[2]}",
                     f"④{cleaning_tasks[3]}：{rotated_residents[3]}",
                     f"⑤{cleaning_tasks[4]}：{rotated_residents[4]}"]

    # Join the lines into a single string
    message = '\n' + '\n'.join(message_lines)

    return message

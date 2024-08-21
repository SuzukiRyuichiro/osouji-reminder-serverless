import requests
import os
from datetime import datetime, timedelta, timezone

def run(event, context):
    url = "https://notify-api.line.me/api/notify"
    access_token = os.environ['LINE_NOTIFY_CLIENT_TOKEN']
    headers = {'Authorization': 'Bearer ' + access_token}
    tomorrow = get_tomorrow(event['time'])
    trash_tomorrow = determine_trash(tomorrow)
    if trash_tomorrow is None:
      return

    message = f'明日のゴミは{trash_tomorrow}です。'
    payload = {'message': message}
    r = requests.post(url, headers=headers, params=payload,)

def determine_trash(date):
    day_of_week = date.weekday()  # Monday is 0 and Sunday is 6
    day_of_month = date.day

    if day_of_week == 0 or day_of_week == 3:  # Monday or Thursday
        return "燃えるゴミ"
    elif day_of_week == 1:  # Tuesday
        return "プラスチック"
    elif day_of_week == 2:  # Wednesday
        # Check if it's the 2nd or 4th Wednesday
        week_of_month = (day_of_month - 1) // 7 + 1
        if week_of_month == 2 or week_of_month == 4:
            return "燃えないゴミ(金属、電池、ガラス、蛍光灯など)"
    elif day_of_week == 4:  # Friday
        return "資源(紙、缶、瓶、ペットボトルなど)"


def get_tomorrow(datetime_str):
  date_obj = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%SZ")
  # Convert the datetime object to Japan Standard Time (JST)
  jst = timezone(timedelta(hours=9))
  date_obj = date_obj.astimezone(jst)

  # Calculate the next day at 7 AM JST
  next_morning = (date_obj + timedelta(days=1)).replace(hour=7, minute=0, second=0, microsecond=0)

  return next_morning


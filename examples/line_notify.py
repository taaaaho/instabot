import requests

url = "https://notify-api.line.me/api/notify"
access_token = 'your access token'
headers = {'Authorization': 'Bearer ' + access_token}

def notify(message):
  payload = {'message': message}
  requests.post(url, headers=headers, params=payload,)


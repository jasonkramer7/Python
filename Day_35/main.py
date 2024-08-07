import requests
from twilio.rest import Client
import os


account_sid = "AC5c1b5e0a2c71fe68e4196be5dc03ab6d"
auth_token = os.environ.get("OWM_AUTH_TOKEN")
api_key = os.environ.get("OWM_API_KEY")
endpoint = "https://api.openweathermap.org/data/2.5/forecast"
params = {
    "lat": "41.110630",
    "lon": "-95.987060",
    "appid": api_key
}
response = requests.get(endpoint, params=params)
weather_data = response.json()
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain☔️☔",
        from_="+18667815947",
        to="+14028851281"
    )
    print(message.status)


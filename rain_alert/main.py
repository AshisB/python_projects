import os
import requests
from twilio.rest import Client

# LAT_COR = 27.634990
# LONG_COR = 85.301920

#intiated Twilio Call
message_body=''
account_sid = 'AC02c02af1a60c1c5866da2a2f6c151b22'
auth_token = '47162ec4a93a298a6fb1bb58c27eaa22'
client = Client(account_sid, auth_token)


#intiated Open Weather API Call
api_key='61be1c4a39e15d87f05ecb7d753cec74'
parameters={
    'lat':27.634990,
    'lon':85.301920,
    'appid':api_key,
    'cnt':4
}



OWM_Endpoint='https://api.openweathermap.org/data/2.5/forecast'
response=requests.get(url=OWM_Endpoint,params=parameters)
response.raise_for_status()
weather_data=response.json()
print(weather_data['list'][0]['dt_txt'])


all_ids=[{'weather_id':all_weather['id'],
             'main':all_weather['main'],'description':all_weather['description'],'temperature':weather_item['main']['temp'],'time':weather_item['dt_txt']}
         for weather_item in weather_data['list']
         for all_weather in weather_item['weather']]

if any((int(all_data['weather_id'])<700) for all_data in all_ids):
    message_body='Today it might rain,Take an ☂️ with you'
    message = client.messages.create(
        messaging_service_sid='MGb5d2aea1b6951c6e4ca4eb5a5e2ca321',
        body=message_body,
        to='+9779861909242'
    )
    print(message.sid)
else:
    print('Have a good day.Dont worry about umbrella today')

print(all_ids)



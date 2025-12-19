import requests
from datetime import datetime,timedelta
time_record=datetime.now()+timedelta(days=1)


TOMORROW_DATE=time_record.date()
LAT_COR=27.634990
LONG_COR=85.301920


parameters={
    'lat':LAT_COR,
    'lng':LONG_COR,
    'formatted':0,
    'date':TOMORROW_DATE,
    'tzid':'Asia/Kathmandu'
}
response=requests.get(url='https://api.sunrise-sunset.org/json',params=parameters)
print(response.url)
response.raise_for_status()
api_data=response.json()
print(api_data)
sunrise_time=api_data['results']['sunrise']
sunset_time=api_data['results']['sunset']
print(sunrise_time,sunset_time)




sunrise_hour=sunrise_time.split('T')[1].split(':')[0]
sunset_hour=sunset_time.split('T')[1].split(':')[0]
present_hour=time_record.hour
print(present_hour)
import requests
import datetime as dt
import smtplib
import time

LAT_COR = 27.634990
LONG_COR = 85.301920
#functions
def SendMail(message_template,receiver_email):
    sender_email = "nujayabia@gmail.com"
    sender_password = 'sohv mtjp uaye usus'
    message=f'Subject:LOOK AT THE SKY:\n\n{message_template}'
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=sender_email,password=sender_password)
        connection.sendmail(sender_email,receiver_email,message)
        print('mail sent succesfully')

def CheckNight():
    # sunrise_sunset_api part
    parameters = {
        'lat': LAT_COR,
        'lng': LONG_COR,
        'formatted': 0,
    }
    response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters, timeout=10)
    response.raise_for_status()
    api_data = response.json()
    sunrise_time = api_data['results']['sunrise']
    sunset_time = api_data['results']['sunset']

    sunrise_hour = int(sunrise_time.split('T')[1].split(':')[0])  # parameter 1
    sunset_hour = int(sunset_time.split('T')[1].split(':')[0])  ##parameter 2

    time_record = dt.datetime.now()
    present_hour = int(time_record.hour)  # parameter 3
    present_time = time_record.time()
    print(present_time)

    if present_hour < sunrise_hour or present_hour > sunset_hour:#checks if sun is gone?
        return True




def CheckAbove():
    #iss api part
    response_iss=requests.get('http://api.open-notify.org/iss-now.json',timeout=10)
    response_iss.raise_for_status()
    iss_data=response_iss.json()


    iss_long=float(iss_data['iss_position']['longitude'])
    iss_lat=float(iss_data['iss_position']['latitude'])

    print(iss_long)
    print(iss_lat)

    if LAT_COR + 5 >= iss_lat >= LAT_COR - 5 and LONG_COR + 5 >= iss_long >= LONG_COR - 5:  # check if ISS is above head?
        return True


#here we are writing to track and notify


def TrackIss():
    global notification_sent
    if CheckNight() and CheckAbove():
        if not notification_sent:
            message = 'HELLO, ISS is above your head.\nLook up at sky.'
            receiver = 'maharjanashis9@gmail.com'
            SendMail(message, receiver)
            notification_sent = True
    else:
        print('ISS is not visble to you yet')
        notification_sent = False


notification_sent=False

while True:
    TrackIss()
    if CheckNight():
        time.sleep(60)
    else:
        time.sleep(43200)



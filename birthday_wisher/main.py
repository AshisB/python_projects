import smtplib
import pandas as pd
import csv
import datetime as dt
import random
import os
import sys


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Then in your code, use:
# file_path = resource_path("birthdays.csv")

def SendMail(message_template,receiver_email):
    sender_email = "nujayabia@gmail.com"
    sender_password = 'sohv mtjp uaye usus'
    message=f'Subject:Happy Birthday:\n\n{message_template}'
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=sender_email,password=sender_password)
        connection.sendmail(sender_email,receiver_email,message)
        print('mail sent succesfully')









# 1. Update the birthdays.csv
# df=pd.read_csv('./birthdays.csv')
# birthday_data=[{'name':values.name,'email':values.email,'year':values.year,'month':values.month,'day':values.day}for values in df.itertuples()]

with open(resource_path('./birthdays.csv'),'r') as data_file:
    csv_data=csv.DictReader(data_file)
    birthday_data=[values for values in csv_data]

# print(birthday_data)


# 2. Check if today matches a birthday in the birthdays.csv
time_today=dt.datetime.now()
today_tuple=time_today.timetuple()
# print(today_tuple)

#2.a Collecting timestamps of today
month_today=today_tuple.tm_mon
day_today=today_tuple.tm_mday
# hour_today=today_tuple.tm_hour
# min_today=today_tuple.tm_min
# sec_today=today_tuple.tm_sec
final_message=[]
#2.a now looping through our birthday data to  check above time stamps
for birthday in birthday_data:
    # print(f'{type(birthday['month'])}=>{type(month_today) },{birthday['day']}=>{day_today}')
    if int(birthday['month'])==month_today and int(birthday['day'])==day_today:
        print('jackpot')
        random_number=random.randint(1,3)
        with open(resource_path(f'./letter_templates/letter_{random_number}.txt'),'r') as f:
            message_template=f.readlines()
        message_replaced=message_template[0].replace('[NAME]',birthday['name'])
        message_template[0]=message_replaced
        print(message_template)
        message_template=' '.join(message_template)
        print(message_template)
        receiver_email=birthday['email']
        SendMail(message_template,receiver_email)









# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.





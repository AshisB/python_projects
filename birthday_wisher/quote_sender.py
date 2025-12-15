import smtplib
import datetime as dt
import random

with open('quotes.txt','r', encoding='utf-8') as f:
    quotes=f.read()
quotes_list=quotes.split("|")

random_quote=random.choice(quotes_list)#selecting a quote randomly
print(random_quote)


while True:
    record_time = dt.datetime.now()
    week_day = record_time.weekday()
    print(record_time.timetuple().tm_sec)
    if week_day==0 and record_time.timetuple().tm_hour==22 and record_time.timetuple().tm_min==35 and record_time.timetuple().tm_sec<=3:
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            sender_email = "nujayabia@gmail.com"
            sender_password = 'sohv mtjp uaye usus'
            message = f"Subject:Good Evening\n\n{random_quote}"
            receiver_email = "radhakrishna8888@yahoo.com"

            connection.login(sender_email, sender_password)
            connection.sendmail(sender_email, receiver_email, message.encode('utf-8'))
            print('here')
            break













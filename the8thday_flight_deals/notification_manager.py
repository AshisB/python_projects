from twilio.rest import Client
from dotenv import load_dotenv
import os
import smtplib
import textwrap
load_dotenv()
class NotificationManager:
    def __init__(self):
        self.message_body=''
        self.account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        self.auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        self.client = Client(self.account_sid,self.auth_token)
        self.sender_email = os.getenv('SENDER_EMAIL')
        self.sender_password = os.getenv('SENDER_PASSWORD')

    def get_notifications(self,fdata):      
        #messaging started for user
     
        self.message_body = f"FLIGHT:{fdata['city']} £{fdata['grand_total']} {fdata['departure_location']}→{fdata['arrival_location']} {fdata['departure_at'][:10]} {fdata['airline_code']}{fdata['flight_number']} {fdata['stops']}"
        print(self.message_body)
        message=self.client.messages.create(
            messaging_service_sid=os.getenv('MESSAGING_SERVICE_ID'),
            body=self.message_body,
            to=os.getenv('TWILIO_PHONE_NUMBER')
        )
        print(message)
        print('Done succesfully')  
        

    def get_email_notifications(self,fdata,userdata):      
        #messaging started for user
        self.message_body = textwrap.dedent(f"""
        Dear {userdata['whatIsYourFirstName?']} {userdata['whatIsYourLastName?']},                                    
        ✈️✈️✈️ FLIGHT DEAL ALERT ✈️✈️✈️
        
        🏙️  Destination: {fdata['city']}
        💰  Price: {fdata['grand_total']} {fdata['currency']}
        ⏰  Book by: {fdata['last_ticketing_date']}
        
        🛫  Departure: {fdata['departure_location']} at {fdata['departure_at'][:16]}
        🛬  Arrival: {fdata['arrival_location']} at {fdata['arrival_at'][:16]}
        
        ✈️  Flight: {fdata['airline_code']}{fdata['flight_number']}
        🛩️  Aircraft: {fdata['aircraft_type']}
        
        🔥 LIMITED TIME OFFER! 🔥
        Book now and save! 🎉
        """).strip()

        print(self.message_body)
  
        receiver_email=userdata['whatIsYourEmailAddress?']
        with smtplib.SMTP('smtp.gmail.com',587) as connection:
            connection.starttls()
            connection.login(user=self.sender_email,password=self.sender_password)
            connection.sendmail(self.sender_email,receiver_email,self.message_body.encode('utf-8'))
            print('mail sent succesfully')

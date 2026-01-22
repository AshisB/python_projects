import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta
import json

AUTH_URL="https://test.api.amadeus.com/v1/security/oauth2/token"
AMADEUS_BASE_URl="https://test.api.amadeus.com/v1/"


class FlightSearch:
    def __init__(self):
       load_dotenv
       self.amadeus_token=None
       self.token_data=None
       



    def get_access_token(self):
        token_headers={
            "Content-Type": "application/x-www-form-urlencoded"
        }
        token_data={
            "grant_type":"client_credentials",
            "client_id":os.getenv("CLIENT_ID"),
            "client_secret":os.getenv("CLIENT_SECRET")
        }

        token_response=requests.post(url=AUTH_URL,headers=token_headers,data=token_data)
        print(token_response.json())
        token=token_response.json()["access_token"]
        return token
    

    # def get_token(self):

        # try:
        #     if len(self.amadeus_token)==0:
        #         with open("token.json", 'r', encoding='utf-8') as f:
        #             token_data = json.load(f) 
        #         if len(token_data)>0:
        #             now = datetime.now()
        #             present_time=now.timestamp()
        #             if token_data['expiry_time']<present_time:
        #                 self.amadeus_token=token_data['token']
        #             else:
        #                 os.remove("token.json")
        #                 self.get_token()    
        #         else:    
        #             self.amadeus_token=self.get_access_token()
        #             self.write_token_json()
        # except FileNotFoundError:
        #        with open("token.json", 'w') as f:
        #         json.dump({}, f)
        #         self.get_token()           


    def get_token(self):
        try:
            # Initialize if None
            if not self.amadeus_token:
                # Check if token file exists
                if os.path.exists("token.json"):
                    with open("token.json", 'r', encoding='utf-8') as f:
                        self.token_data = json.load(f)
                    
                    # Check if we have valid data
                    self.check_token_expiry()
                else:
                    self.amadeus_token = self.get_access_token()
                    self.write_token_json()
                # If we get here, need new token
                self.amadeus_token = self.get_access_token()
                self.write_token_json()
            else:
                # Check if we have valid data
                self.check_token_expiry()   
        except (FileNotFoundError, json.JSONDecodeError):
            # File doesn't exist or is corrupted
            self.amadeus_token = self.get_access_token()
            self.write_token_json()
          
    def check_token_expiry(self):
        if self.token_data and 'token' in self.token_data:
            present_time = datetime.now().timestamp()
            
            # CORRECTED: Token is valid if expiry_time is GREATER than present
            if self.token_data['expiry_time'] > present_time:
                self.amadeus_token = self.token_data['token']
            else:
                # Token expired - delete and get new
                os.remove("token.json")
                self.amadeus_token = self.get_access_token()
                self.write_token_json()   

    def write_token_json(self):
        #writing it in token txt
        now = datetime.now()
        expiry_time = now + timedelta(minutes=30)
        token_json={
            "token":self.amadeus_token,
            "expiry_time":(expiry_time).timestamp(),
            "human_readable": expiry_time.isoformat(), 
            "formatted": expiry_time.strftime("%Y-%m-%d %H:%M:%S")
        }
        with open("token.json", 'w', encoding='utf-8') as f:
            json.dump(token_json,f,indent=2)       
            
                    

    def get_iata(self,city_name):
        self.get_token()
        city_params={
            "keyword":city_name
        }

        site_url=f'{AMADEUS_BASE_URl}reference-data/locations/cities'
        amadeus_headers={
                "Authorization":f"Bearer {self.amadeus_token}"
            }
        try:   
            response=requests.get(url=site_url,params=city_params,headers=amadeus_headers)
            cities_data=response.json()
            print(cities_data['data'][0]['iataCode']  )
            return cities_data['data'][0]['iataCode']  
        except KeyError:
            self.amadeus_token=self.get_access_token()
            self.write_token_json()
            amadeus_headers={
                "Authorization":f"Bearer {self.amadeus_token}"
            }
            response=requests.get(url=site_url,params=city_params,headers=amadeus_headers)
            cities_data=response.json()
            print(cities_data['data'][0]['iataCode'])
            return cities_data['data'][0]['iataCode']  




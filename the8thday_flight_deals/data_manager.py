import requests
from dotenv import load_dotenv
import os
import json

BASE_URL="https://api.sheety.co/7e931b8e386f9080f71dce71a2bc478d/flightDeals/prices"
USERS_BASE_URL="https://api.sheety.co/7e931b8e386f9080f71dce71a2bc478d/flightDeals/users"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        load_dotenv()
        self.sheety_token=os.getenv('SHEETY_TOKEN')
        self.sheety_headers={
            "Authorization":self.sheety_token
        }
  

    def get_sheety_data(self):
        sheety_response=requests.get(url=BASE_URL,headers=self.sheety_headers)
        self.sheety_data=sheety_response.json()
        return self.sheety_data

    def get_sheety_users_data(self):
        sheety_response=requests.get(url=USERS_BASE_URL,headers=self.sheety_headers)
        self.sheety_data=sheety_response.json()
        return self.sheety_data

    def edit_sheety_data(self,sheety_data):
        put_url=f'{BASE_URL}/{sheety_data['id']}'
        sheety_params={
            "price":{
                "city":sheety_data['city'],
                "iatacode":sheety_data['iatacode'],
                "lowestprice":sheety_data['lowestprice'],
            }    
        }
        print(put_url)
        print(sheety_params)
        # # adding row to your sheet
        sheety_reponse=requests.put(url=put_url,headers=self.sheety_headers,json=sheety_params)
        print(sheety_reponse)
        print(sheety_reponse.text)
        return sheety_reponse.text
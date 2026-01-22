import os
import requests
from dotenv import load_dotenv
from flight_search import FlightSearch
from pprint import pprint
import json
import time
from datetime import datetime, timedelta

AMADEUS_BASE_URL="https://test.api.amadeus.com/"



class FlightData:
    def __init__(self):
       load_dotenv
       flightobj=FlightSearch()
       flightobj.get_token()
       self.amadeus_token=flightobj.amadeus_token
       self.ourcheapestflights={}
       
  

    def get_flight_data(self,country,is_direct=True):
        flight_url=f'{AMADEUS_BASE_URL}v2/shopping/flight-offers' 
        amadeus_headers={
                "Authorization":f"Bearer {self.amadeus_token}"
            }
        # Calculate dates
        today = datetime.now()
        tomorrow=today+ timedelta(days=1)
        future_date = today + timedelta(days=180)

        # Format for Amadeus
        # departure_start = tomorrow.strftime("%Y-%m-%d")
        # departure_end = future_date.strftime("%Y-%m-%d")
        departure_start = "2026-03-20"
        
        if is_direct==True:
            direct_indirect="true"
        else:
            direct_indirect="false"    

        flight_params={
            "originLocationCode": "LON",         
            "destinationLocationCode": f"{country['iatacode']}",     
            "departureDate": f"{departure_start}",      
            "adults": 1,   
            "currencyCode": "GBP",               
            "maxPrice": country['lowestprice'], 
            "nonStop":direct_indirect
        }




        print(flight_url)
        print(flight_params)
        print(amadeus_headers)
        print(f"this is  direct_indirect{direct_indirect}") 

        flightdata_response=requests.get(url=flight_url,headers=amadeus_headers,params=flight_params)
        time.sleep(5)
        allflight_data=flightdata_response.json()
        print(allflight_data)
        if len(allflight_data)!=0:
            self.get_cheapest_flight(allflight_data,country)
    

    def get_cheapest_flight(self,allflight_data,country):
        json_string = json.dumps(allflight_data)
        with open("flight.json", 'w', encoding='utf-8') as f:
            json.dump(json_string,f)       


        with open('flight.json','r',encoding='utf-8') as f:
            data=json.load(f)
            flight_data=json.loads(data)
        # pprint(flight_data['meta'])    
        # pprint(json.dumps(flight_data['data'][:2],indent=2))
        prices=flight_data['data']
        allpricelist=[]


        # prices=allflight_data['data']
        # allpricelist=[]

        for price in prices:
            prices_dict={}
            stops=[]
            prices_dict['city']=country['city']
            prices_dict['last_ticketing_date']=price['lastTicketingDate']
            prices_dict['currency']=price['price']['currency']
            prices_dict['grand_total']=price['price']['grandTotal']
            prices_dict['departure_at']=price['itineraries'][0]['segments'][0]['departure']['at']
            prices_dict['departure_location']=price['itineraries'][0]['segments'][0]['departure']['iataCode']
            prices_dict['arrival_at']=price['itineraries'][0]['segments'][0]['arrival']['at']
            prices_dict['airline_code'] = price['itineraries'][0]['segments'][0]['carrierCode']
            prices_dict['flight_number'] = price['itineraries'][0]['segments'][0]['number']
            prices_dict['aircraft_type'] = price['itineraries'][0]['segments'][0]['aircraft']['code']
            segments = price['itineraries'][0]['segments']
           
            for segment in segments:
                stops.append(segment['arrival']['iataCode'])    
            if len(segments)>0:
                stops.append(str(len(segments)))
                prices_dict['stops']="->".join(stops)
            prices_dict['arrival_location'] =segments[-1]['arrival']['iataCode']
            prices_dict['arrival_at']=segments[-1]['arrival']['at']
            allpricelist.append(prices_dict)
            
        print(allpricelist)    
        print(json.dumps(allpricelist,indent=2))

        for item in allpricelist:
            if float(item['grand_total'])<=float(country['lowestprice']):
                print('we found your flight')
                if not item['city'] in self.ourcheapestflights: 
                    self.ourcheapestflights[item['city']]=item
                else:
                    if item['grand_total']< self.ourcheapestflights[item['city']]['grand_total']:
                        self.ourcheapestflights[item['city']]=item 
  
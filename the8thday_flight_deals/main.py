#This file will need to use the DataManager,FlightSearch,
#  FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flightdata import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
import time
import random
from pprint import pprint


if __name__=="__main__":
    
    sheetyobj=DataManager()
    flightsearchobj=FlightSearch()
    flightdataobj=FlightData()
    notificationobj=NotificationManager()

    prices=sheetyobj.get_sheety_data()['prices']

    # This code here fills the iataCode to the sheety data
    for item in prices:
        if len(item['iatacode'])==0:
            delay=random.randint(4,12)
            item['iatacode']=flightsearchobj.get_iata(item['city'])
            time.sleep(delay)
            sheetyobj.edit_sheety_data(item)
            time.sleep(delay)
        else:
            print('Already present data')    
    print('succesfully done')

    def get_cheapest_flight(is_direct=True):
        #This code here  will get data from sheety and runs loop 
        sheetydata=sheetyobj.get_sheety_data()['prices']
        for country in sheetydata:
            print(country)
            flightdataobj.get_flight_data(country,is_direct)
        print(flightdataobj.ourcheapestflights)
        cheapest_flights=flightdataobj.ourcheapestflights
        return cheapest_flights


    cheapest_flights=get_cheapest_flight()
    if len(cheapest_flights)==0:
        cheapest_flights=get_cheapest_flight(is_direct=False)

    if len(cheapest_flights)>0:
        users_data=sheetyobj.get_sheety_users_data()
        for user in users_data['users']:
            cheapest_flight_data =list(cheapest_flights.values())
            for flight in cheapest_flight_data:
                notificationobj.get_email_notifications(flight,user)
    else:
        print('Sorry!No Flights')        

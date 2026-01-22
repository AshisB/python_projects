import json
from pprint import pprint
with open('flight.json','r',encoding='utf-8') as f:
    data=json.load(f)
    flight_data=json.loads(data)
# pprint(flight_data['meta'])    
pprint(json.dumps(flight_data['data'][:3],indent=2))
prices=flight_data['data']
allpricelist=[]

for price in prices:
    prices_dict={}
    prices_dict['last_ticketing_date']=price['lastTicketingDate']
    prices_dict['currency']=price['price']['currency']
    prices_dict['grand_total']=price['price']['grandTotal']
    prices_dict['departure_date']=price['itineraries'][0]['segments'][0]['departure']['at']
    prices_dict['departure_iata']=price['itineraries'][0]['segments'][0]['departure']['iataCode']
    prices_dict['arrival_at']=price['itineraries'][0]['segments'][0]['arrival']['at']
    allpricelist.append(prices_dict)
print(allpricelist)    
print(json.dumps(allpricelist,indent=2))


# for item in allpricelist:
#     if float(item['grand_total'])<=float(pricewehave):
        # call twillio app
        # add item data
import requests
import json
import datetime as dt
from twilio.rest import Client
import os
from dotenv import load_dotenv


load_dotenv()

# test_symbols = ["TSLA", "AAPL", "GOOGL", "MSFT"]
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"



#intiated Twilio Call
message_body=''
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)



def get_stock_data():
    #for stock data
    stock_params={
        'function':'TIME_SERIES_DAILY',
        'symbol':STOCK,
        'outputsize':'compact',
        'apikey':os.getenv('STOCK_API')
    }


    response=requests.get(STOCK_ENDPOINT,params=stock_params)
    response.raise_for_status()
    stock_data=response.json()

    return stock_data



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
def get_news(from_date,to_date,topic):
    print(f"{from_date},{to_date},{topic}")
    news_params={
        'q':topic,
        'apiKey':os.getenv('NEWS_API'),
        'sortBy':'relavancy',
        'language':'en',
        'from':from_date,
        'to':to_date,
        'pageSize':10
    }


    response=requests.get(NEWS_ENDPOINT,params=news_params)
    response.raise_for_status()
    news_data=response.json()
    return news_data
    print(news_data)


stock_data=get_stock_data()  #received stock data

#******************************meta data part*******************************
meta_data=stock_data["Meta Data"]
latest_date=meta_data['3. Last Refreshed']
symbols=meta_data['2. Symbol']

latest_date_iso=dt.date.fromisoformat(latest_date)
week_before_iso=latest_date_iso-dt.timedelta(days=7)
#******************************meta data part***************************


daily_data=stock_data['Time Series (Daily)']
daily_data_list=list(daily_data.values())[:2]
# print(daily_data_list)

day_before_yesterday_close=float(daily_data_list[1]['4. close'])
yesterday_close=float(daily_data_list[0]['4. close'])

total_diff=day_before_yesterday_close-yesterday_close
total_diff_percentage=round(abs((total_diff/yesterday_close)*100))

stock_message=f'{STOCK}:🔻{total_diff_percentage}%' if day_before_yesterday_close>yesterday_close else f'{STOCK}:🔺{total_diff_percentage}%' 

print(stock_message)


if total_diff_percentage>=5:
    news_data=get_news(latest_date_iso,week_before_iso,COMPANY_NAME)
    sliced_stock_data=news_data['articles'][:2]
    
    #messaging started for user
    for s_data in sliced_stock_data:
        message_body=f"\n{stock_message}\n{s_data['title']}"
        message=client.messages.create(
            messaging_service_sid=os.getenv('MESSAGING_SERVICE_ID'),
            body=message_body,
            to=os.getenv('TWILIO_PHONE_NUMBER')
        )
    else:
        print('Done succesfully')    

else:
    print('stock change below 5%')       












#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


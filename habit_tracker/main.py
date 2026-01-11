import os
import requests
from  dotenv import load_dotenv
import webbrowser
import datetime as dt

load_dotenv()
SITE_ENPOINT='https://pixe.la'
APP_USERNAME=os.getenv('MY_APP_USERNAME')
TOKEN=os.getenv('TOKEN')
GRAPH_ID='graph1'
graph_headers={
    "X-USER-TOKEN":TOKEN
    }

# 1)crearting user for habit tracking
# USER_CREATE_ENDPOINT=SITE_ENPOINT+'/v1/users'
# user_params={
#     "token":"sdkkksdjsh67453hd83jnsd",
#     "username":"ashisb",
#     "agreeTermsOfService':"yes",
#     "notMinor":"yes"
# }

# response=requests.post(url=USER_CREATE_ENDPOINT,json=user_params)
# print(response.text)


# 2)Create a graph definition
graph_endpoint=f'{SITE_ENPOINT}/v1/users/{APP_USERNAME}/graphs'
print(graph_endpoint)
graph_params={
    "id":"graph1",
    "name":"reading_habit_graph",
    "unit":"pages",
    "type":'int',
    "color":"ajisai",
    "timezone":"Asia/Kathmandu"
}
# graph_headers={
#     "X-USER-TOKEN":TOKEN
#     }
# graph_response=requests.post(url=graph_endpoint,json=graph_params,headers=graph_headers)
# print(graph_response.text)


# 3)See the graph that you have created


graph_url=f'{SITE_ENPOINT}/v1/users/{APP_USERNAME}/graphs/{GRAPH_ID}'
# webbrowser.open(graph_url)
# print(f"Opening Url: {graph_url}")

# 4) POST VALUE TO GRAPH
entry_graph_endpoint=f'{SITE_ENPOINT}/v1/users/{APP_USERNAME}/graphs/{GRAPH_ID}'
graph_headers={
    "X-USER-TOKEN":TOKEN
    }

today=str(dt.datetime.now().date())
pixel_date=today.replace("-","")
# or use strftime('%y%m%d',today)
print(pixel_date)
print(today)
entry_params={
    "date":pixel_date,
    "quantity":'1'
}
print(entry_graph_endpoint)
# entry_graph_response=requests.post(url=entry_graph_endpoint,headers=graph_headers,json=entry_params)
# print(entry_graph_response.text)


# 5) now to update the data or pixels we can do
datetoupdate=dt.datetime(year=2026,month=1,day=8)
datetoupdate_pixel=datetoupdate.strftime('%Y%m%d')
print(datetoupdate_pixel)
update_pixel_endpoint=f"{SITE_ENPOINT}/v1/users/{APP_USERNAME}/graphs/{GRAPH_ID}/{datetoupdate_pixel}"

update_params={
    "quantity":"1"
}

# update_response=requests.put(url=update_pixel_endpoint,headers=graph_headers,json=update_params)
# print(update_response.text)


# 6)Delete pixel
datetodelete=dt.datetime(2026,1,9)
datetodelete_pixel=datetodelete.strftime('%Y%m%d')
delete_pixel_endpoint=f"{SITE_ENPOINT}/v1/users/{APP_USERNAME}/graphs/{GRAPH_ID}/{datetodelete_pixel}"
# delete_pixel_reponse=requests.delete(url=delete_pixel_endpoint,headers=graph_headers)
# print(delete_pixel_reponse.text)

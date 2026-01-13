import os
import requests
from dotenv import load_dotenv
import json
import datetime as dt

load_dotenv()

BASE_URL="https://app.100daysofpython.dev"
API_KEY=os.getenv('API_KEY')
APP_ID=os.getenv('APP_ID')
SHEETY_TOKEN=os.getenv('SHEETY_TOKEN')

def workout():
    app_headers={
        "x-app-id":APP_ID,
        "x-app-key":API_KEY
    }

    workout_params={
        "query":input('Tell me which exercise you did? '),
        "weight_kg":70,
        "height_cm":171,
        "age":29,
        "gender":"male"
    }
    entry_endpoint=f'{BASE_URL}/v1/nutrition/natural/exercise'
    app_response=requests.post(url=entry_endpoint,json=workout_params,headers=app_headers)
    app_response.raise_for_status()
    workout_data=app_response.json()
    return workout_data
    # json_string = json.dumps(workout_data, indent=4)
    # print(json_string)



# get healths data/healthz
def get_healthz():
    get_healthz_response=requests.get(url=f'{BASE_URL}/healthz')
    return get_healthz_response.json()


def get_googlesheetdata():
    sheety_header={
        "Authorization": SHEETY_TOKEN
    }
    sheety_endpoint='https://api.sheety.co/7e931b8e386f9080f71dce71a2bc478d/workoutTracking/sheet1'
    sheety_get_data=requests.get(url=sheety_endpoint,headers=sheety_header)
    return sheety_get_data.text



def entry2sheet():

    # for the sheety data
    sheety_header={
        "Authorization": SHEETY_TOKEN
    }

    today=dt.datetime.now()
    date_today=today.strftime('%d/%m/%Y')
    time_today=today.strftime('%H:%M:%S')
    # print(time_today)


    workout_datas=workout()
    workout_data_all=workout_datas['exercises']
    print(workout_datas)
    for workout_data in workout_data_all:
        workout_name=workout_data['name'].title()
        workout_duration=workout_data['duration_min']
        workout_calories=workout_data['nf_calories']

        sheety_params={
            "sheet1":{
                "date":date_today,
                "time":time_today,
                "exercise":workout_name,
                "duration":workout_duration,
                "calories":workout_calories
        }
        }

        # print(sheety_params)
        # # adding row to your sheet
        sheety_endpoint='https://api.sheety.co/7e931b8e386f9080f71dce71a2bc478d/workoutTracking/sheet1'
        sheety_reponse=requests.post(url=sheety_endpoint,headers=sheety_header,json=sheety_params)
        return sheety_reponse.text




success=entry2sheet()

print(success)
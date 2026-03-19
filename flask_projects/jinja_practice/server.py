from flask import Flask,render_template
from datetime import datetime as dt
import requests

AGIFY_ENDPOINT="https://api.agify.io"
GENDERIZE_ENDPOINT="https://api.genderize.io"

now=dt.now()
year=now.year

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",copyright_year=year)

@app.route("/guess/<username>")
@app.route("/guess/<username>/<country>")
def person(username,country="US"):
    user_params={
        "name":username,
        "country_id":country.upper()
    }

    gender_params={
        "name": username
    }

    agify_response=requests.get(url=AGIFY_ENDPOINT,params=user_params)
    agify_response.raise_for_status()
    agify_data=agify_response.json()
    print(agify_data['name'])

    genderize_response=requests.get(url=GENDERIZE_ENDPOINT,params=gender_params)
    genderize_response.raise_for_status()
    genderize_data=genderize_response.json()
    print(genderize_data['gender'])

    return render_template("person.html",person_name=username.title(),age=agify_data['age'],gender=genderize_data['gender'])

if __name__=="__main__":
    app.run(debug=True)
from flask import Flask, render_template,redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField,URLField,TimeField,SelectField,SubmitField
from wtforms.validators import DataRequired
import csv
from dotenv import  load_dotenv
import os
from datetime import datetime
load_dotenv()

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
bootstrap=Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired('Input required!!')],render_kw={"class": "mb-3"})
    location = URLField('Location', validators=[DataRequired('Input required!!')],render_kw={"class": "mb-3"})
    open =TimeField('Open At', validators=[DataRequired('Input required!!')],render_kw={"class": "mb-3"})
    close =TimeField('Close At', validators=[DataRequired('Input required!!')],render_kw={"class": "mb-3"})
    coffee =SelectField(
        'Coffee Ratings',
        validators=[DataRequired('Input required!!')],
        choices = [
            ('☕', '☕ - Poor'),
            ('☕☕', '☕☕ - Fair'),
            ('☕☕☕', '☕☕☕ - Good'),
            ('☕☕☕☕', '☕☕☕☕ - Very Good'),
            ('☕☕☕☕☕', '☕☕☕☕☕ - Excellent')
        ],
        render_kw={"class": "mb-3"})
    wifi = SelectField(
        'Wifi Ratings',
        validators=[DataRequired('Input required!!')],
        choices=[
            ('🌐','🌐 - No Internet(1/5)'),
            ('📶📶', '📶📶 - Poor (2/5)'),
            ('📶📶📶 ', '📶📶📶 - Average (3/5)'),
            ('📶📶📶📶', '📶📶📶📶 - Good (4/5)'),
            ('📶📶📶📶📶', '📶📶📶📶📶 - Excellent (5/5)')
        ],
        render_kw={"class": "mb-3"})
    power = SelectField(
        'Power Ratings',
        validators=[DataRequired('Input required!!')],
        choices=[
                ('❌', '❌ - No outlets'),
                ('🔌🔌', '🔌🔌 - Very limited'),
                ('🔌🔌🔌', '🔌🔌🔌 - Some outlets'),
                ('🔌🔌🔌🔌', '🔌🔌🔌🔌 - Many outlets'),
                ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌 - Outlets + USB everywhere')
            ],
        render_kw={"class": "mb-3"})
    submit = SubmitField('Submit')


# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=['GET','POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe_name=form.cafe.data
        location=form.location.data


        dt1 = form.open.data
        dt2 = form.close.data
        opentime = dt1.strftime("%I:%M %p").lstrip("0")  # Remove leading zero
        closetime = dt2.strftime("%I:%M %p").lstrip("0")


        coffee=form.coffee.data
        wifi=form.wifi.data
        power=form.power.data
        print("True")
        form_data=[cafe_name,location,opentime,closetime,coffee,wifi,power]

        with open('cafe-data.csv', 'a', encoding='UTF-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(form_data)
            print('print successfully')
        return redirect('/cafes')
    return render_template('add.html', form=form)


@app.route('/cafes')
def show_cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)

    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)

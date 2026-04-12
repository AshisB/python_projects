from flask import FLASk,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import Integer,String,Float


app=FLASk(__name__)

@app.route("/")
def home():
    return ('index.html')



if __name__==("__main__"):
    app.run(debug=True)
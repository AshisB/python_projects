from flask import Flask,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import Integer,String,Float


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///new-books-collection.db"
db=SQLAlchemy()
db.init_app(app)

class Books(db.Model):
    id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]=mapped_column(unique=True)
    author:Mapped[str]
    rating:Mapped[float]
with app.app_context():
    db.create_all()    




@app.route("/")
def home():
    return ('index.html')



if __name__==("__main__"):
    app.run(debug=True)
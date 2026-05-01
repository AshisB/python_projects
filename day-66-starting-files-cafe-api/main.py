from flask import Flask, jsonify, render_template, request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean,select,update,delete,func,desc
import json

from sqlalchemy.testing.config import ident

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def random():
    query=db.select(Cafe).order_by(func.random()).limit(1)
    cafe_data=db.session.execute(query).scalar()
    # Convert to dictionary
    cafe_dict = {column.name: getattr(cafe_data,column.name) for column in cafe_data.__table__.columns}
    print(json.dumps(cafe_dict, indent=2))
    return jsonify(cafe_dict)


@app.route("/all")
def get_all():
    query=select(Cafe).order_by(Cafe.coffee_price)
    cafes=db.session.execute(query).scalars().all()
    cafe_list=[{column.name:getattr(cafe,column.name) for column in cafe.__table__.columns} for cafe in cafes]
    print(json.dumps(cafe_list,indent=2))
    return jsonify(cafe_list)

@app.route("/search")
def get_cafe():
    location=request.args.get('loc')
    query=select(Cafe).order_by(desc(Cafe.name)).where(Cafe.location==location)
    cafes=db.session.execute(query).scalars().all()

    cafe_list=[{column.name:getattr(cafe,column.name) for column in cafe.__table__.columns} for cafe in cafes]
    return jsonify(cafe_list)

@app.route("/add-cafe", methods=['GET', 'POST'])
def addCafe():
    # Use request.args for URL query parameters
    newcafe = Cafe(
        coffee_price=request.args.get('coffee_price'),  # Fixed spelling
        name=request.args.get('name'),
        map_url=request.args.get('map_url'),
        img_url=request.args.get('img_url'),
        location=request.args.get('location'),
        has_sockets=bool(int(request.args.get('has_sockets', 0))),  # Convert to boolean
        has_toilet=bool(int(request.args.get('has_toilet', 0))),
        has_wifi=bool(int(request.args.get('has_wifi', 0))),
        can_take_calls=bool(int(request.args.get('can_take_calls', 0))),
        seats=int(request.args.get('seats', 0))  # Convert to integer
    )
    db.session.add(newcafe)
    db.session.commit()
    return jsonify({'success': 'Cafe has been succesfully added.'})

@app.route("/update-price/<int:id>",methods=["PATCH"])
def updatePrice(id):
    try:
        price =request.args.get('coffee_price')
        
        if not price:
            return jsonify({"error": "Price is required"}), 400
        
        query=update(Cafe).where(Cafe.id==id).values(coffee_price=price)
        db.session.execute(query)
        db.session.commit()
        return jsonify({"Success":"Successfully price updated."}),200
    except Exception as e:
        return jsonify({"Not found":f"Sorry!There was problem.{str(e)}"}),500   
    
@app.route("/report-closed/<int:id>",methods=["DELETE"])   
def deleteCafe(id):
    apiKey=request.args.get("api-key")
    if apiKey:
        if apiKey=="TopSecretAPIKey":
            cafe=db.session.get(Cafe,id)
            if cafe:
                db.session.delete(cafe)
                db.session.commit()
                return jsonify({"success":"Successfully deleted"}),200
            else:
                return jsonify({"Not Found":"Sorry!cafe not found"}),400

            
        else:
            return jsonify({"error":"Sorry!Please use correct API KEY"}),403
    else:        
        return jsonify({"error":"API KEY NEEDED!Please use API KEY"}),401
# Mahadev Har Har Mahadev
# HTTP GET - Read Record
# Shambhoo
# HTTP POST - Create Record
#  Tu hi he shambhu tu hi he 
# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)

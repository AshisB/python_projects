from flask import Flask,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import Integer,String,Float,update,delete


class Base(DeclarativeBase):
    pass

db=SQLAlchemy(model_class=Base)


class Books(db.Model):
    id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]=mapped_column(unique=True)
    author:Mapped[str]
    rating:Mapped[float]

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///new-books-collection.db"
db.init_app(app)

with app.app_context():
    db.create_all()

###########################CREATE##########################
# with app.app_context():
#     new_book=Books(title="HITCSlkl",author="TJ Klune",rating=9)
#     db.session.add(new_book)
#     db.session.commit()

# with app.app_context():
#     new_books=[
#         Books(title="Fairy",author='Julian D. Costa',rating=6),
#         Books(title="Swan Husk",author='Cobian Shierk',rating=7),
#         Books(title='Geneva Orchestra',author='K.M. Srivastav',rating=8)
#     ]
#     db.session.add_all(new_books)
#     db.session.commit()

#*********************************READ*****************************

# with app.app_context():
#     books=db.session.execute(db.select(Books).where(Books.author=="TJ Klune")).scalars()
#     for book in books:
#         print(f"Title={book.title},Rating={book.rating}")
#     result=db.session.execute(db.select(Books).order_by(Books.rating))
#     print(result)
#     all_books=result.scalars()
#     for book in all_books:
#         print(f"Title={book.title},Rating={book.rating}")

#**********************************UPDATE***************************************


# with app.app_context():
#     query=update(Books).where(Books.id==3).values(author="C.R.Mahalaxmi")
#     db.session.execute(query)
#     db.session.commit()


#**************************Delete*******************************
# with app.app_context():
#     book=db.session.execute(db.select(Books).where(Books.title=="HITCS")).scalar()
#     db.session.delete(book)
#     db.session.commit()
# with app.app_context():
#     query=delete(Books).where(Books.author=="TJ Klune")
#     db.session.execute(query)
#     db.session.commit()


@app.route("/")
def home():
    return ('index.html')



if __name__==("__main__"):
    app.run(debug=True)
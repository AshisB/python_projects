from flask import Flask, render_template, url_for,redirect,flash
from flask_bootstrap import Bootstrap5
from dotenv import load_dotenv
import os
from functools import wraps
from flask_toastr import Toastr


from app_class.form_class import FillForm
from Models.Book import Books
from Models.Base import db


load_dotenv()

#***************************DATABASE CONNECTION******************************
app=Flask(__name__)
app.config['SECRET_KEY']=os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"]=os.getenv("DATABASE_NAME")
bootstrap=Bootstrap5(app)
db.init_app(app) # from her db knows about app and its config

with app.app_context(): #creates table
    db.create_all()

# Initialize Flask-Toastr
toastr = Toastr(app)


#****************************************exception handling*********************************************
def handle_book_errors(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
            return redirect(url_for('home'))
    return decorated


@app.route("/")
def home():
    books=Books.get_all_books()
    columns=Books.get_column_names()

    if len(books)>0:
        return render_template("index.html",books=books,all_column=columns)
    else:
        return render_template("index.html")


@app.route("/add-book",methods=['GET','POST'])
@handle_book_errors
def add_book():
    form=FillForm()
    if form.validate_on_submit():
        title=form.title.data
        author=form.author.data
        rating=form.rating.data

        form_data={
            'title':title,
            'author':author,
            'rating':rating
        }
        print(form_data)
        Books.add_book(form_data)
        flash('Book added successfully!', 'success')
        return redirect(url_for('home'))

    return render_template('form.html',form=form,pagename="add")


@app.route("/edit-book/<int:id>",methods=['GET','POST'])
@handle_book_errors
def edit_book(id):
    bookinfo=Books.get_book_info(id)
    if bookinfo:
        form=FillForm(obj=bookinfo)
    else:
        return "Book not found", 404

    if form.validate_on_submit():
        title=form.title.data
        author=form.author.data
        rating=form.rating.data

        form_data={
            'title':title,
            'author':author,
            'rating':rating
        }
        print(form_data)
        Books.edit_book(id,form_data)
        flash('Book edited successfully!', 'success')
        return redirect(url_for('home'))

    return render_template('form.html',form=form,pagename="edit")


@app.route("/delete-book/<int:id>")
@handle_book_errors
def delete_book(id):
    Books.delete_book(id)
    flash('Book deleted successfully!', 'success')
    return redirect(url_for('home'))




if __name__==("__main__"):
    app.run(debug=True)

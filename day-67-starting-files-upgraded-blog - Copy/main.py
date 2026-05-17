import datetime
from functools import wraps
from flask import Flask, render_template, redirect, url_for,flash
from flask_bootstrap import Bootstrap5
from flask_migrate import Migrate
from flask_ckeditor import CKEditor
from datetime import date
from dotenv import load_dotenv
import os
from flask_wtf import CSRFProtect
from werkzeug.security import generate_password_hash

from models.Base import db
from models.User import User
from app_class.user_class import UserForm,UserData,LoginForm
from models.Comment import Comment
# from app_class.user_class import CommentForm,CommentData
from models.Post import BlogPost
from app_class.post_class import FillForm,PostData

from flask_toastr import Toastr



load_dotenv()
migrate=Migrate()
app = Flask(__name__)
app.config['SECRET_KEY'] =os.getenv('SECRET_KEY')
csrf = CSRFProtect(app)
Bootstrap5(app)
ckeditor=CKEditor(app)
toastr=Toastr(app)


# CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] =os.getenv('DATABASE_URI')
db.init_app(app)  #connection of database to flask application
migrate.init_app(app,db)


#****************************************exception handling*********************************************
def handle_movie_errors(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            error_msg = "Sorry! There is some problem while performing your task."
            return redirect(url_for('home',error=error_msg))
    return decorated





@app.route('/')
def home():
    posts = BlogPost.getAll()
    return render_template("index.html", all_posts=posts)


@app.route('/post/<int:post_id>')
@handle_movie_errors
def show_post(post_id):
    requested_post = BlogPost.getPost(post_id)
    return render_template("post.html", post=requested_post)



@app.route('/add-post',methods=['GET','POST'])
@handle_movie_errors
def add_post():
    form=FillForm()
    if form.validate_on_submit():
        now=datetime.datetime.now()
        year=now.year
        month=now.strftime("%B")
        day=now.day
        date=f"{day} {month},{year}"
        form_data={
            'title':form.title.data,
            'subtitle':form.subtitle.data,
            'date':date,
            'body':form.body.data,
            'author':form.author.data,
            'img_url':form.img_url.data
        }
        form_obj=PostData(form_data)
        BlogPost.addPost(form_obj)
        flash('Post added successfully!!','success')
        return redirect(url_for('home'))
    return render_template("make-post.html",form=form,pagename="add")


@app.route("/edit-post/<int:post_id>",methods=['GET','POST'])
@handle_movie_errors
def edit_post(post_id):
    post_data=BlogPost.getPost(post_id)
    form = FillForm(obj=post_data)
    if form.validate_on_submit():
        form_data = {
            'title': form.title.data,
            'subtitle': form.subtitle.data,
            'date': date,
            'body': form.body.data,
            'author': form.author.data,
            'img_url': form.img_url.data
        }
        form_obj=PostData(form_data)
        BlogPost.editPost(form_obj,post_id)
        flash('Blog edited succesfully.','success')
        return redirect(url_for('home'))
    return render_template('make-post.html',form=form,pagename="edit")



@app.route("/delete-post/<int:post_id>")
@handle_movie_errors
def delete_post(post_id):
    BlogPost.deletePost(post_id)
    flash('Post successfully deleted','success')
    return redirect(url_for('home'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


#**************************************USERS*************************************
@app.route("/register",methods=['GET','POST'])
def register():
    form=UserForm()
    if form.validate_on_submit():
        hash_password=generate_password_hash(form.password.data,method="pbkdf2:sha256",salt_length=8)
        user_data={
            'name':form.name.data,
            'email':form.email.data,
            'password':hash_password
        }
        user_obj=UserData(user_data)
        User.addUser(user_obj)
        flash("User has been successfully added.",'success')
        return redirect(url_for('home'))
    return render_template('register.html',form=form,pagename="register")


@app.route("/login",methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        pass
    return render_template('login.html',loginform=form,pagename="login")

if __name__ == "__main__":
    app.run(debug=True, port=5003)

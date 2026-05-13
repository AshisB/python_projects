from flask import Flask, render_template, request, url_for,session, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, select
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_wtf.csrf import CSRFProtect
from flask_toastr import Toastr


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
csrf = CSRFProtect(app)
toastr=Toastr(app)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB
login_manager=LoginManager()
login_manager.init_app(app)
# CREATE DATABASE
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column()
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect("/secrets")
    if request.method == 'GET':
        return render_template("register.html")
    if request.method=='POST':
        if db.session.execute(select(User).where(User.email == request.form.get("email"))).scalar():
            flash("Email already has been taken","error")
            return render_template("register.html")
        hash_password=generate_password_hash(request.form.get("password"),method="pbkdf2:sha256",salt_length=8)
        new_user=User(
            name=request.form.get("name"),
            email=request.form.get("email"),
            password=hash_password,
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash(f"Dear {current_user.name},Welcome to dashboard", "success")
        return redirect(url_for("secrets"))
    return None


@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect("/secrets")
    if request.method == 'GET':
        return render_template("login.html")

    if request.method == 'POST':
        query=select(User).where(User.email==request.form.get("email"))
        user=db.session.execute(query).scalar()
        if user and check_password_hash(user.password,request.form.get("password")):
            login_user(user)
            print(user)
            print(request.form.get("password"))
            session['name'] = request.form.get("name")
            flash(f"Dear {current_user.name},Welcome to dashboard", "success")
            return redirect(url_for("secrets"))
        else:
            flash("Sorry wrong credentials", "error")
            return render_template("login.html")



@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html",name=current_user.name)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out Successfully!!.Please visit us again","info")
    return redirect(url_for("home"))


@app.route('/download/<path:filename>')
@login_required
def download(filename):
    return send_from_directory("static/files",filename,as_attachment=False,download_name="flask_cs_download.pdf")



if __name__ == "__main__":
    app.run(debug=True)

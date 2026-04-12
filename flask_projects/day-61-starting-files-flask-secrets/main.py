from flask import Flask, render_template,redirect,url_for,session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired,Length,email

app = Flask(__name__)
app.config['SECRET_KEY']='secret key'
bootstrap = Bootstrap(app)


class LoginForm(FlaskForm):
    username=StringField('username',validators=[InputRequired('username required'),email(message='Email must  Have @ and format example@xyz.com !!')])
    password=PasswordField('password',validators=[InputRequired('Password required'),Length(min=8,max=15,message='Username should be of length 8 to 15 !!')])
    submit=SubmitField('submit')

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login",methods=['GET','POST'])
def login():
    formobj=LoginForm()
    if formobj.validate_on_submit():
        username_data=formobj.username.data
        session['username']=username_data
        return redirect(url_for('dashboard'))
    return render_template('login.html',form=formobj)


@app.route("/dashboard",methods=['GET'])
def dashboard():

    if 'username' in session:
        return render_template('success.html',username=session.get('username'))
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)

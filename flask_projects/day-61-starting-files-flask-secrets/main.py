from flask import Flask, render_template,redirect,url_for,session
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired,Length

app = Flask(__name__)
app.config['SECRET_KEY']='secret key'
bootstrap = Bootstrap5(app)


class LoginForm(FlaskForm):
    username=StringField('username',validators=[InputRequired('username required'),Length(min=5,max=10,message='username should be of length 5 to 10')])
    password=PasswordField('password',validators=[InputRequired('Password required'),Length(min=5,max=10,message='username should be of length 5 to 10')])
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

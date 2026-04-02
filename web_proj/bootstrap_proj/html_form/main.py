from flask import Flask,render_template,request

app=Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login",methods=['GET','POST'])
def go_dashboard():
    error='Sorry we are unable to login'
    if request.method =='POST':
        return render_template('dashboard.html',username=request.form.get('username'))
    else:
        return render_template('index.html',error=error)


if __name__==("__main__"):
    app.run(debug=True)
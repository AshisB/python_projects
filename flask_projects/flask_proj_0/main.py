from flask import Flask
from functools import wraps
import os

# decorator
def make_bold(func):
    @wraps(func)    #ths creates new wrapper every time
    def main_wrapper():
        return (f'<strong>{func()}</strong>')
    return main_wrapper

def make_emphasis(func):
    @wraps(func)
    def main_wrapper():
        return (f'<em>{func()}</em>')
    return main_wrapper

def make_underlined(func):
    @wraps(func)
    def main_wrapper():
        return (f'<u>{func()}</u>')
    return main_wrapper





app = Flask(__name__)
print("Flask's root_path:", app.root_path)

@app.route("/")

def hello_world():
    print(__name__)
    return ('<h1 style="text-align:center">Hello,World!</h1>'
            '<p>This is an info box.</p>'
            '<img src="https://media3.giphy.com/media'
            '/v1.Y2lkPTc5MGI3NjExMDVnNGI1ZmNlZzB2anU1b2FscWRucXV5ZDlrdWVheDluN2F0d2h0YSZlcD12M'
            'V9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HJ5ouJLslLKBIEiHg5/giphy.gif" height=200 width=200>')



@app.route("/byee")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye World"

@app.route("/user/<username>/<int:number>/")
def greet(username,number):
    return f"Hello {username+'12'}, how are you? Your age is {number}"
#
if __name__=="__main__":
     app.run(debug=True)
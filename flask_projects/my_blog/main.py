from flask import Flask, render_template,request
import requests
from blog import Blog
import datetime
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)

@app.context_processor
def inject_now():
    return {'now': datetime.datetime.now()}

def get_all_blogs():
    blog_objects = []
    blog_response=requests.get("https://api.npoint.io/86778b065b6fb0bbbe39")
    blog_response.raise_for_status()
    blog_data=blog_response.json()
    for blog in blog_data:
        blog_obj=Blog(blog['id'],blog['title'],blog['subtitle'],blog['body'],blog['author'],blog['published_at'])
        blog_objects.append(blog_obj)
    return blog_objects

@app.route('/blog')
@app.route('/')
def home():
    all_blogs=get_all_blogs()
    image_path = f'assets/img/home-bg.jpg'
    title = 'My Blog'
    subtitle = 'Expression of words.'
    return render_template("index.html",pagedata=title,blogs=all_blogs,image_header=image_path,subtitle=subtitle)

@app.route('/blog/<int:index>')
def read_blog(index):
    blogs=get_all_blogs()
    blogdetail=[blog for blog in blogs if blog.id==index]
    image_path = f'assets/img/post-bg.jpg'
    title = blogdetail[0].title
    subtitle = blogdetail[0].subtitle
    print(blogdetail)
    return render_template("post.html",blog_detail=blogdetail[0],pagedata=title,image_header=image_path,subtitle=subtitle)



@app.route('/about')
def about():
    image_path=f'assets/img/about-bg.jpg'
    title='About Me'
    subtitle='This is what I do.'
    return render_template('about.html',pagedata=title,image_header=image_path,subtitle=subtitle)

@app.route('/contact',methods=['GET','POST'])
def contact():
    if request.method=='GET':
        image_path = f'assets/img/contact-bg.jpg'
        title='Contact Me'
        subtitle='Have questions?I have answers.'
        return render_template('contact.html',pagedata=title,image_header=image_path,subtitle=subtitle)
    elif request.method=='POST':
        image_path = f'assets/img/contact-bg.jpg'
        title = 'Thank you for giving us feedback'
        subtitle = 'Have questions?I have answers.'
        print(request.method)
        print(request.form)
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        message=request.form.get('message')
        final_message=f"""
        from={name}
        email={email}
        phone={phone}
        message={message}
        """
        result=SendMail(final_message,'maharjanashis9@gmail.com')
        if result:
            return render_template('contact.html', pagedata=title, image_header=image_path, subtitle=subtitle,message="Thank you for giving us feedback")
        else:
            return render_template('contact.html', pagedata=title, image_header=image_path, subtitle=subtitle,
                                   message="Sorry,There was problem while sending message")

def SendMail(message_template,receiver_email):
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    message=f'Subject:Blog Feedback:\n\n{message_template}'
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=sender_email,password=sender_password)
        connection.sendmail(sender_email,receiver_email,message)
        print('mail sent succesfully')
        return True


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template
import requests
from blog import Blog
import datetime


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

@app.route('/contact')
def contact():
    image_path = f'assets/img/contact-bg.jpg'
    title='Contact Me'
    subtitle='Have questions?I have answers.'
    return render_template('contact.html',pagedata=title,image_header=image_path,subtitle=subtitle)

if __name__ == "__main__":
    app.run(debug=True)

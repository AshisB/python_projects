# from flask import Flask, render_template
# import requests
#
#
# app = Flask(__name__)
#
# def get_all_blogs():
#     blog_response=requests.get("https://api.npoint.io/c790b4d5cab58020d391")
#     blog_response.raise_for_status()
#     blog_data=blog_response.json()
#     return blog_data
#
# @app.route('/blog')
# @app.route('/')
# def home():
#     all_blogs=get_all_blogs()
#     return render_template("2.html",blog_data=all_blogs)
#
# @app.route('/blog/<blog_id>')
# def read_blog(blog_id):
#     blogs=get_all_blogs()
#     print(blogs)
#     print(blog_id)
#     blogdetail=[blog for blog in blogs if int(blog['id'])==int(blog_id)]
#     print(blogdetail)
#     return render_template("1.html",blog_detail=blogdetail[0])
#
# if __name__ == "__main__":
#     app.run(debug=True)

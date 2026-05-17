from flask_wtf import FlaskForm
from markupsafe import Markup
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL, Length
from flask_ckeditor import  CKEditorField


class PostData():
    def __init__(self,form_data):
        self.title = form_data['title']
        self.subtitle = form_data['subtitle']
        self.date = form_data['date']
        self.body = form_data['body']
        self.author = form_data['author']
        self.img_url = form_data['img_url']



class FillForm(FlaskForm):
    title=StringField("Post Title:",validators=([DataRequired('Required!!'),Length(1,250,message="Title must be between 1 and 250 character")]),render_kw={"placeholder": "Post title","id":"movie-title"})
    subtitle=StringField("Subtitle:",validators=([DataRequired('Required!!')]))
    # date=StringField("Published Date:",validators=([DataRequired('Required!!')]))
    body=CKEditorField("Description:", validators=([DataRequired('Required!!')]))
    author=StringField("Author:",validators=([DataRequired('Required!!')]))
    img_url=StringField("Image Link:", validators=([DataRequired('Required!!')]))
    submit = SubmitField('Submit',render_kw={"class":"btn btn-success"})

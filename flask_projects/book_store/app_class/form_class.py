from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FloatField
from wtforms.validators import  NumberRange,DataRequired


class FillForm(FlaskForm):
    title=StringField('Book Title',validators=[DataRequired('Book Title required!!')])
    author=StringField('Author',validators=[DataRequired('Author required!!')])
    rating=FloatField('Rating', validators=[DataRequired('Rating required!!'), NumberRange(min=0,max=10,message="Rating range is from 0-10" )])
    submit=SubmitField('Submit',render_kw={"class": "mt-3"})


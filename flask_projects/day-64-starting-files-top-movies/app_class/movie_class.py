from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,FloatField,TextAreaField,SubmitField
from wtforms.validators import DataRequired, Length, Optional, URL

class MovieData():
    def __init__(self,form_data):
        self.title =form_data['title']
        self.year = form_data['year']
        self.description = form_data['description']
        self.rating = form_data['rating']
        self.ranking = form_data['ranking']
        self.review = form_data['review']
        self.img_url = form_data['img_url']

class FillForm(FlaskForm):
    title=StringField('Movie Title:',validators=([DataRequired('Required!!'),Length(1,250,message="Title must be between 1 and 250 character")]),render_kw={"placeholder": "Movie title", "id": "movie-title"})
    year = IntegerField('Year:', validators=([DataRequired('Required!!')]),render_kw={"placeholder": "Release year", "id": "movie-year"})
    description = TextAreaField('Description:', validators=([Length(0,600,message="Too Long"),Optional()]),render_kw={"placeholder": "Release year", "id": "movie-description"})
    rating = FloatField('Rating:', validators=([DataRequired('Required!!')]),render_kw={"placeholder": "0-10", "id": "movie-rating"})
    ranking = IntegerField('Ranking:', validators=([Optional()]),render_kw={"id": "movie-ranking"})
    review= TextAreaField('Review',validators=([Length(0,300,message="Too Long")]), render_kw={"placeholder": "Your personal review", "id": "movie-review", "rows": 3})
    img_url = StringField('Movie Image:', validators=([Optional()]),render_kw={"placeholder": "Poster URL", "id": "movie-img_url"})
    submit=SubmitField('Submit')
from functools import wraps
from flask import Flask, render_template, redirect, url_for, flash, session, request, jsonify
from flask_bootstrap import Bootstrap5
import requests
from dotenv import load_dotenv
import os
from models.Base import db
from models.Movie import Movie
from app_class.movie_class import FillForm,MovieData
from flask_toastr import Toastr


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
Bootstrap5(app)
toastr=Toastr(app)

# CREATE DB
app.config['SQLALCHEMY_DATABASE_URI']=os.getenv("DATABASE_URI")
db.init_app(app)
with app.app_context():
    db.create_all()

# CREATE TABLE

#****************************************exception handling*********************************************
def handle_movie_errors(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            error_msg = "Sorry! There is some problem while performing your task."
            return redirect(url_for('home',error=error_msg))
    return decorated





@app.route("/")
def home():
    error = request.args.get('error')
    if error:
        flash(error, 'error')
        return redirect(url_for('home'))
    movies=Movie.getMovies()
    print(movies)
    if len(movies)>0:
        print(movies)
        return render_template("index.html",movies=movies)
    else:
        return render_template("index.html")



@app.route("/add-movie",methods=['GET','POST'])
@handle_movie_errors
def add_movie():
    form=FillForm()
    if form.validate_on_submit():
        form_data = {
            'title': form.title.data,
            'year': form.year.data,
            'description': form.description.data,
            'rating': form.rating.data,
            'ranking': form.ranking.data,
            'review': form.review.data,
            'img_url': form.img_url.data,
        }

        Movie.addMovie(MovieData(form_data))
        flash('Movie added successfully!', 'success')
        return redirect(url_for('home'))
    return render_template("form.html",form=form,pagename="add")


# @app.route("/add-movie", methods=['GET', 'POST'])
# def add_movie():
#     form = FillForm()
#     if form.validate_on_submit():
#         # Remove csrf_token and submit from form.data
#         movie_data = {k: v for k, v in form.data.items()
#                       if k not in ['csrf_token', 'submit']}
#
#         # Pass unpacked dictionary directly
#         Movie.addMovie(**movie_data)
#
#         flash('Movie added successfully!', 'success')
#         return redirect(url_for('home'))
#
#     return render_template("form.html", form=form, pagename="add")

@app.route("/edit-movie/<int:id>",methods=['GET','POST'])
@handle_movie_errors
def editMovie(id):
    movie = Movie.getMovie(id)
    if movie:
        form=FillForm(obj=movie)
    else:
        return "Movie not found", 404

    if form.validate_on_submit():
        form_data = {
            'title': form.title.data,
            'year': form.year.data,
            'description': form.description.data,
            'rating': form.rating.data,
            'ranking': form.ranking.data,
            'review': form.review.data,
            'img_url': form.img_url.data,
        }
        print(form_data)

        Movie.editMovie(id,MovieData(form_data))
        flash('Movie edited successfully!', 'success')
        return redirect(url_for('home'))
    return render_template("form.html",form=form,pagename="edit")


@app.route("/delete-movie/<int:id>",methods=['GET'])
@handle_movie_errors
def deleteMovie(id):
    movie = Movie.getMovie(id)
    if movie:
        Movie.deleteMovie(id)
        flash('Movie deleted successfully!', 'success')
    else:
        flash('sorry!! There was a problem while deleting', 'error')
    return redirect(url_for('home'))


@app.route('/api/search-movie-select')
def search_movie_select2():
    query = request.args.get('q', '')
    if len(query) < 3:
        return jsonify({"results": []})
    url = "https://api.themoviedb.org/3/search/movie"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.getenv('TMDB_READ_ACCESS_TOKEN')}"
    }
    params={
        "query":query
    }
    response = requests.get(url, headers=headers,params=params)
    response.raise_for_status()
    print(response.text)
    data=response.json()
    print(data)
    results = []
    for movie in data.get('results', []):
        print(movie.get('title'))
        year = movie.get('release_date', '')[:4] if movie.get('release_date') else 'N/A'
        results.append({
            "id": movie.get('id'),  # ✅ Safer! Won't crash if 'id' missing
            "text": f"{movie.get('title', 'Unknown')} ({year})"  # ✅ Even safer with default
        })
    print(results)
    return jsonify({"results": results})




@app.route('/movie-details/<int:id>')
def movie_details(id):

    url = f"https://api.themoviedb.org/3/movie/{id}"
    print(url)

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.getenv('TMDB_READ_ACCESS_TOKEN')}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        movie = response.json()

        year = (
            movie.get('release_date', '')[:4]
            if movie.get('release_date')
            else ''
        )

        poster_path = movie.get('poster_path')

        img_url = (
            f"https://image.tmdb.org/t/p/w500{poster_path}"
            if poster_path else ''
        )

        return jsonify({
            "title": movie.get('title', ''),
            "year": year,
            "description": movie.get('overview', ''),
            "rating": movie.get('vote_average', ''),
            "img_url": img_url
        })

    except requests.exceptions.RequestException as e:
        return jsonify({
            "error": str(e)
        }), 500



if __name__ == '__main__':
    app.run(debug=True)

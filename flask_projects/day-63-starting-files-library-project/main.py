from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def call_database():
    db = sqlite3.connect("books-collection.db")
    cursor=db.cursor()
    return {'db':db,'cursor':cursor}

# conn=call_database()
#
# conn['cursor'].execute("DROP TABLE IF EXISTS books")
# conn['cursor'].execute("CREATE TABLE books"
#                "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
#                "title VARCHAR(250) NOT NULL UNIQUE,"
#                "author VARCHAR(150) NOT NULL,"
#                "rating FLOAT NOT NULL)"
#                )

all_books = []


@app.route('/')
def home():
    return render_template('index.html',books=all_books)


@app.route("/add",methods=['GET','POST'])
def add():
    if request.method=='POST':
        book_dict = {'title': request.form.get('title'),
                     'author': request.form.get('author'),
                     'rating': request.form.get('rating')}
        conn=call_database()
        conn['cursor'].execute("INSERT INTO books (title,author,rating) VALUES (?,?,?)",
                       (request.form.get("title"),request.form.get("author"),float(request.form.get("rating")))
                       )
        conn['db'].commit()

        all_books.append(book_dict)
        print(all_books)
        return redirect(url_for('home'))
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)


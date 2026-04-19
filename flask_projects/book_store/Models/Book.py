from Models.Base import Base,db
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import update,delete,select

class Books(db.Model):
    __tablename__ = 'books'

    id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]=mapped_column(unique=True)
    author:Mapped[str]
    rating:Mapped[float]


    @classmethod
    def add_book(cls,form_data):
        new_book=cls(title=form_data['title'],author=form_data['author'],rating=form_data['rating'])
        db.session.add(new_book)
        db.session.commit()

    @classmethod
    def edit_book(cls,id,form_data):
        bookinfo=cls.get_book_info(id)
        if bookinfo:
            bookinfo.title=form_data['title']
            bookinfo.author = form_data['author']
            bookinfo.rating = form_data['rating']
        db.session.commit()

    @classmethod
    def delete_book(cls, id):
        query=delete(cls).where(cls.id==id)
        db.session.execute(query)
        db.session.commit()





    @classmethod
    def get_all_books(cls):
        query=select(cls).order_by(cls.id.desc())
        books=db.session.execute(query)
        return books.scalars().all()

    @classmethod
    def get_book_info(cls,id):
        query = select(cls).where(cls.id==id)
        book = db.session.execute(query)
        return book.scalar()



    @classmethod
    def get_column_names(cls):
        # Define custom display names
        display_names = {
            'id': 'ID',
            'title': 'Book Title',
            'author': 'Author Name',
            'rating': 'Rating (0-10)'
        }

        # Get actual column names and map to display names
        return [display_names.get(col.name, col.name) for col in cls.__table__.columns]


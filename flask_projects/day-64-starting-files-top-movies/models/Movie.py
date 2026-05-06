from datetime import datetime,timezone
from app_class.movie_class import MovieData
from models.Base import Base,db
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String,Float,update,delete,select



class Movie(db.Model):
    __tablename__='movies'

    id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]=mapped_column(String(25),unique=True,nullable=False)
    year:Mapped[int]=mapped_column(nullable=False)
    description:Mapped[str]=mapped_column(String(600),nullable=True)
    rating:Mapped[float]=mapped_column(default=0.0)
    ranking:Mapped[int]=mapped_column(unique=True,nullable=True)
    review:Mapped[str]=mapped_column(String(25),nullable=True)
    img_url:Mapped[str]=mapped_column(String(300),default='default-movie.jpg')

    created_at:Mapped[datetime]=mapped_column(default=datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))


    @classmethod
    def addMovie(cls,form_data:MovieData):
        new_movie=cls(
            title= form_data.title,
            year= form_data.year,
            description= form_data.description,
            rating= form_data.rating,
            ranking= form_data.ranking,
            review= form_data.review,
            img_url= form_data.img_url,
        )
        db.session.add(new_movie)
        db.session.commit()

    @classmethod
    def getMovies(cls):
        query=select(cls).order_by(cls.rating.asc())
        movies=db.session.execute(query)
        movies_list=movies.scalars().all()

        for i in range(len(movies_list)):
            movies_list[i].ranking=len(movies_list)-i
        return movies_list

    @classmethod
    def getMovie(cls,id):
        query = select(cls).where(cls.id==id)
        movie = db.session.execute(query)
        return movie.scalar()

    @classmethod
    def editMovie(cls,id,form_data:MovieData):
        movie=cls.getMovie(id)
        print(form_data)
        print(form_data.title)
        if movie:
            movie.title= form_data.title
            movie.year= form_data.year
            movie.description= form_data.description
            movie.rating= form_data.rating
            movie.ranking= form_data.ranking
            movie.review= form_data.review
            movie.img_url= form_data.img_url
        db.session.commit()


    @classmethod
    def deleteMovie(cls, id):
        movie = cls.getMovie(id)
        if movie:
            query=delete(cls).where(cls.id==id)
            db.session.execute(query)
            db.session.commit()

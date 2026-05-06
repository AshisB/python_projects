from models.Base import db
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String, Float, update, Integer, Text, select, delete, asc
from datetime import datetime,timezone
from app_class.post_class import PostData





# CONFIGURE TABLE
class BlogPost(db.Model):
    __tablename__='posts'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    created_at: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc),
                                                 onupdate=datetime.now(timezone.utc))


    @classmethod
    def getAll(cls):
        query=select(cls).order_by(asc(cls.title))
        posts=db.session.scalars(query)
        return posts.all()

    @classmethod
    def addPost(cls,form_obj:PostData):
        new_post=cls(
            title=form_obj.title,
            subtitle=form_obj.subtitle,
            date=form_obj.date,
            body=form_obj.body,
            author=form_obj.author,
            img_url=form_obj.img_url
        )
        db.session.add(new_post)
        db.session.commit()


    @classmethod
    def editPost(cls,form_obj:PostData,post_id):
        post=cls.getPost(post_id)
        if post:
            post.title=form_obj.title
            post.subtitle = form_obj.subtitle
            post.body = form_obj.body
            post.author = form_obj.author
            post.img_url = form_obj.img_url
        db.session.commit()


    @classmethod
    def deletePost(cls,post_id):
        query=delete(cls).where(cls.id==post_id)
        db.session.execute(query)
        db.session.commit()


    @classmethod
    def getPost(cls,post_id):
        query=select(cls).where(cls.id==post_id)
        post_data=db.session.scalar(query)
        print(post_data)
        return post_data

    # @classmethod
    # def getPost(cls, post_id):
    #     post_data = db.session.get(cls, post_id)
    #     return post_data

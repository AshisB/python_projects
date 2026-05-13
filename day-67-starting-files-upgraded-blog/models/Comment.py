from models.Base import db
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import String, Float, update, Integer, Text, select, delete, asc, ForeignKey
from datetime import datetime,timezone
from app_class.post_class import PostData





# CONFIGURE TABLE
class Comment(db.Model):
    __tablename__ = 'comments'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc),
                                                 onupdate=datetime.now(timezone.utc))


    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    comment_by = relationship('User', back_populates='comments')


    post_id: Mapped[int] = mapped_column(Integer, ForeignKey('posts.id', ondelete='CASCADE'), nullable=False)
    post = relationship('BlogPost', back_populates='comments')
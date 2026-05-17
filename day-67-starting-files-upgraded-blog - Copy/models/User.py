from models.Base import db
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import String, Float, update, Integer, Text, select, delete, asc
from datetime import datetime,timezone
from app_class.post_class import PostData
import enum
from app_class.user_class import UserData


class UserRole(enum.Enum):
    USER = 'user'
    ADMIN = 'admin'


# CONFIGURE TABLE
class User(db.Model):
    __tablename__='users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    email: Mapped[str] = mapped_column(String(250), nullable=False,unique=True)
    password: Mapped[str] = mapped_column(Text, nullable=False)
    role: Mapped[UserRole] = mapped_column(db.Enum(UserRole), nullable=False, default=UserRole.USER)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc),
                                                 onupdate=datetime.now(timezone.utc))

    # foreign key
    posts_added= relationship('BlogPost', back_populates='added_by', lazy=True,
                         foreign_keys='BlogPost.added_by_id')
    posts_updated= relationship('BlogPost', back_populates='updated_by', lazy=True,
                         foreign_keys='BlogPost.updated_by_id')
    comments = relationship('Comment', back_populates='comment_by', lazy=True,
                            cascade='all, delete-orphan')


    @classmethod
    def addUser(cls,form_obj:UserData):
        new_user=cls(
            name=form_obj.name,
            email=form_obj.email,
            password=form_obj.password
        )
        db.session.add(new_user)
        db.session.commit()
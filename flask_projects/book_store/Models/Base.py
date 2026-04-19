from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import update,delete

class Base(DeclarativeBase):
    pass

db=SQLAlchemy(model_class=Base)
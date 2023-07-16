from sqlalchemy.orm import  sessionmaker, declarative_base
from sqlalchemy import create_engine


engine = create_engine("sqlite:///database.db")
session_maker = sessionmaker(bind=engine)

Base = declarative_base()
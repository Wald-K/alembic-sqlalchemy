from sqlalchemy.orm import  sessionmaker
from sqlalchemy import create_engine


engine = create_engine("sqlite:///database.db")
session_maker = sessionmaker(bind=engine)

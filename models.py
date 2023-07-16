from sqlalchemy.orm import declarative_base, Mapped, mapped_column
import datetime
from sqlalchemy import func
from db import session_maker

Base = declarative_base()

class UserModel(Base):
    __tablename__ = "user"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    birth: Mapped[datetime.date] = mapped_column(nullable=True)
    created: Mapped[datetime.datetime] = mapped_column(insert_default=func.now())
    



example_users = [
    UserModel(first_name="Wald", last_name="Mickiewicz", birth=datetime.datetime(1972, 3, 18)),
    UserModel(first_name="Roman", last_name="Black", birth=datetime.datetime(1970, 4, 9)),
]

def create_users():
    with session_maker() as session:
        for user in example_users:
            session.add(user)
        session.commit()
        

# create_users()
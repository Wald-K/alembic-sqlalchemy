from sqlalchemy.orm import declarative_base, Mapped, mapped_column
import datetime
from sqlalchemy import func
from db import session_maker, Base


class UserModel(Base):
    __tablename__ = "user"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    birth: Mapped[datetime.datetime] = mapped_column(nullable=True)
    created: Mapped[datetime.datetime] = mapped_column(insert_default=func.now())
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    


def create_users(users_list):
    with session_maker() as session:
        for user in users_list:
            session.add(user)
        session.commit()
        print(f"{len(users_list)} Users created")
        
def show_users():
    with session_maker() as session:
        users = session.query(UserModel).all()
        if users:
            for user in users:
                print(user.full_name)
        else:
            print("No users in Database")
        

import datetime
from models import create_users, show_users, UserModel



example_users = [
    UserModel(first_name="Wald", last_name="Mickiewicz", birth=datetime.datetime(1972, 3, 18)),
    UserModel(first_name="Roman", last_name="Black", birth=datetime.datetime(1970, 4, 9)),
]


# create_users(example_users)
# show_users()
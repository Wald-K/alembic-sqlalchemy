
# Alembic-sqlalchemy

Short example alembic use for sqlalchemy migrations.



# Steps

1. Create migrations init
```
alembic init migrations
``` 
where:

`migrations` - directory where migrations will be stored.
`env.py` - file with configuration of alembic
`versions` - folder for migrations files
`alembic.ini` - file to specific db connections
Change 
`sqlalchemy.url = driver://user:pass@localhost/dbname` -> `sqlite:///database.db` in `alembic.ini`

2. In file `env.py` - change sections `# add your model's MetaData object here`

3. Insert models info to `models.py` file.

4. Create migration file.

```
alembic revision --autogenerate -m "Create user model"
```

In folder `migrations\versions` new migration file is created.

5. Put changes from migrations file to database.
```
alembic upgrade heads
```

6. Put example data to database.

Uncomment `create_users(example_users)` and run:

```
python main.py
```

7. Show data from database.

Uncomment `show_users())` and run:

```
python main.py
```






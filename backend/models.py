import os
from datetime import datetime
from sqlalchemy import (Column, String,
                        Integer, DateTime,
                        ForeignKey, create_engine)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json
import psycopg2

database_filename = os.environ.get("DATABASE", "database.db")
project_dir = os.path.dirname(os.path.abspath(__file__))
# database_path = os.environ['DATABASE_URL']
# conn = psycopg2.connect(database_path, sslmode='require')


database_name = "imdb"
database_path = "postgres://{}:{}@{}/{}".format(
    'postgres',
    'Fall2018',
    'localhost:5432',
    database_name
    )

# database_path = os.environ['DATABASE_URL']


db = SQLAlchemy()


def migrate_db(app):
    migrate = Migrate(app, db)
    return migrate


'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


'''
to create and drop databse tables and start over
'''


def db_drop_and_create_all():
    # db.drop_all()
    db.create_all()


# Association Table
class Cast(db.Model):
    __tablename__ = 'cast'
    actor_id = db.Column(db.Integer(), db.ForeignKey(
        'actor.id'), primary_key=True, nullable=True)
    movie_id = db.Column(db.Integer(), db.ForeignKey(
        'movie.id'), primary_key=True, nullable=True)

    def __init__(self, actor_id, movie_id):
        self.actor_id = actor_id
        self.movie_id = movie_id

    def format(self):
        return {"actor_id": self.actor_id, "movie_id": self.movie_id}

    def get_cast(self):
        return {
            "actor_id": self.actor_id,
            "movie_id": self.movie_id
        }

    def long(self):
        return {
            "actor_id": self.actor_id,
            "movie_id": self.movie_id
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.format())


'''
Movie is a parent
Have id, title and release date
'''


class Movie(db.Model):
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    release_date = db.Column(db.Integer, nullable=False)
    movie_genrs = db.Column(String(200))

    def short(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'movie_genrs': self.movie_genrs,
        }

    def long(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'movie_genrs': self.movie_genrs
        }

    def __repr__(self):
        return json.dumps(self.short())

    def __init__(self, title, movie_genrs, release_date):
        self.title = title
        self.movie_genrs = movie_genrs
        self.release_date = release_date

    def get_movie(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'movie_genrs': self.movie_genrs
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'movie_genrs': self.movie_genrs,
            'release_date': self.release_date
        }


'''
Actor
Have id, name, age, gender and foreign key with class Movie
'''


class Actor(db.Model):
    __tablename__ = "actor"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)

    def short(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
        }

    def __repr__(self):
        return f"<Actor {self.id} {self.name} {self.age} {self.gender}>"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_actor(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.format())

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }

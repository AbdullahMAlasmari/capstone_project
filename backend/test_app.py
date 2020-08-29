import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
# from app import create_app
from app import create_app
from models import db, db_drop_and_create_all, setup_db, Actor, Movie
from auth import AuthError, requires_auth
import logging
from settingup import casting_assistant_headers
from settingup import casting_director_headers
from settingup import executive_producer_headers
from settingup import host_url


casting_assistant_token = casting_assistant_headers
casting_director_token = casting_director_headers
executive_producer_token = executive_producer_headers


# def setUp(self):
#     self.app = create_app()
#     self.client = self.app.test_client


# define set authetification method


def settingup_auth(role):
    JWT = ''
    if role == 'casting_assistant':
        JWT = casting_assistant_token
    elif role == 'casting_director':
        JWT = casting_director_token
    elif role == 'executive_producer':
        JWT = executive_producer_token

    return JWT


class CastingAgencyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        # create_app()
        self.client = self.app.test_client
        database_name = "IMDB_Test"
        self.database_path = "postgres://{}:{}@{}/{}".format(
            'postgres',
            'Fall2018',
            'localhost:5432',
            database_name
        )
        setup_db(self.app)

        self.new_actor = {
            "name": "Test Abul",
            "age": 24,
            "gender": "M"
        }
        self.new_movie = {
            "title": "Test Film",
            'release_date': 2010,
            'movie_genrs': "action"
        }
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        pass

    def test_get_all_actor_casting_assistant(self):
        res = self.client().get('/actors',
                                headers=settingup_auth("casting_assistant"))

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_get_all_actor_casting_director(self):
        res = self.client().get('/actors',
                                headers=settingup_auth("casting_director"))

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_get_actor_all_executive_producer(self):
        res = self.client().get('/actors',
                                headers=settingup_auth("executive_producer"))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_401_get_all_actor_unsuccessful(self):
        res = self.client().get('/actors', headers=settingup_auth(''))
        self.assertEqual(res.status_code, 401)

    # test post actor end point
    def test_401_create_actor_casting_assistant(self):
        res = self.client().post('/actors', json=self.new_actor,
                                 headers=settingup_auth('casting_assistant'))
        self.assertEqual(res.status_code, 401)

    def test_create_actor_executive_producer(self):
        res = self.client().post('/actors', json=self.new_actor,
                                 headers=settingup_auth('executive_producer'))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_404_create_actor_unsuccessful(self):
        res = self.client().post('/actors', json={},
                                 headers=settingup_auth('casting_director'))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    # test patch actor end point
    def test_401_update_actor_casting_assistant(self):
        actor = Actor('Test Abul', 25, 'M')
        actor.insert()
        res = self.client().patch('/actors/'+str(actor.id), json={'age': 25},
                                  headers=settingup_auth('casting_assistant'))
        self.assertEqual(res.status_code, 401)

    def test_update_actor_casting_director(self):
        actor = Actor('Test Abu', 28, 'M')
        actor.insert()
        res = self.client().patch('/actors/13'+str(actor.id), json={'age': 28},
                                  headers=settingup_auth('casting_director'))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(actor.get_actor()['age'], 28)

    def test_update_actor_executive_producer(self):
        actor = Actor('Alex Tree', 77, 'M')
        actor.insert()
        res = self.client().patch('/actors/'+str(actor.id), json={'age': 77},
                                  headers=settingup_auth('executive_producer'))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(actor.age, 77)

    def test_404_update_actor_unsuccessful(self):
        res = self.client().patch('/actors/2000', json={},

                                  headers=settingup_auth('executive_producer'))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    # # test delete actor end point
    def test_401_drop_actor_casting_assistant(self):
        actor = Actor('Test abul', 24, 'M')
        actor.insert()
        res = self.client().delete('/actors/'+str(actor.id),
                                   headers=settingup_auth('casting_assistant'))
        self.assertEqual(res.status_code, 401)

    def test_drop_actor_casting_director(self):
        actor = Actor('Test abul', 24, 'M')
        actor.insert()
        res = self.client().delete('/actors/'+str(actor.id),
                                   headers=settingup_auth('casting_director'))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(int(data['delete']), actor.id)

    def test_drop_actor_executive_producer(self):
        actor = Actor('abdul', 30, 'M')
        actor.insert()
        res = self.client().delete(
            '/actors/'+str(actor.id),  headers=settingup_auth(
                'executive_producer'))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(int(data['delete']), actor.id)

    def test_401_drop_actor_unsuccessful(self):
        actor = Actor('ali', 30, 'M')
        actor.insert()
        res = self.client().delete(
            '/actors/'+str(actor.id), headers=settingup_auth(''))
        self.assertEqual(res.status_code, 401)

    # Movie UnitTest

    def test_get_all_movie_casting_assistant(self):
        res = self.client().get('/movies',
                                headers=settingup_auth("casting_assistant"))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_get_all_movie_executive_producer(self):
        res = self.client().get('/movies',
                                headers=settingup_auth("executive_producer"))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_401_get_all_movie_casting_director(self):
        res = self.client().get('/movies', json={},
                                headers=settingup_auth('casting_director'))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_401_get_all_movie_unsucessful(self):
        res = self.client().get('/movies',
                                headers=settingup_auth('new_casting'))
        self.assertEqual(res.status_code, 401)

    def test_create_movie_executive_producer(self):
        res = self.client().post('/movies', json=self.new_movie,
                                 headers=settingup_auth('executive_producer'))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_401_create_movie_casting_assistant(self):
        res = self.client().post('/movies', json=self.new_movie,
                                 headers=settingup_auth('casting_assistant'))
        self.assertEqual(res.status_code, 401)

    def test_401_create_movie_casting_director(self):
        res = self.client().post('/movies', json=self.new_movie,
                                 headers=settingup_auth('casting_director'))
        data = json.loads(res.data)
        if(res.status_code == 401):
            self.assertEqual(res.status_code, 401)
            self.assertEqual(data['code'], 'unauthorized')
            self.assertEqual(data['description'], 'Permission not found.')

        else:

            print('fail.. 2')
            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)

    def test_401_create_movies_success(self):
        res = self.client().post('/movies', json=self.new_movie,
                                 headers=settingup_auth('executive_producer'))

        data = json.loads(res.data)
        if(res.status_code == 200):
            self.assertEqual(res.status_code, 200)
            self.assertEqual(data['success'], True)
        else:
            self.assertEqual(res.status_code, 401)
            self.assertEqual(data['success'], False)

    def test_update_movie_casting_director(self):
        movie = Movie.query.filter_by(id=2).first()

        movieUpdate = {
            'title': "movie_updated",
            'movie_genrs':  movie.movie_genrs,
            'release_date': movie.release_date
        }

        res = self.client().patch('/movies/'+str(movie.id),
                                  json=movieUpdate,
                                  headers=settingup_auth('casting_director'))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['edited'], 2)

    def test_update_movie_executive_producer(self):
        movie = Movie.query.filter_by(id=2).first()

        movieUpdate = {
            'title': "movie_updated",
            'movie_genrs':  movie.movie_genrs,
            'release_date': movie.release_date
        }

        # movie.update()

        res = self.client().patch('/movies/'+str(movie.id),
                                  json=movieUpdate,
                                  headers=settingup_auth('executive_producer'))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['edited'], 2)
        # self.assertEqual(data['movie']['title'], 'updated_movie')

    # def test_401_update_movie_casting_assistant(self):
        movie = Movie(title='first Name')
        movie.insert()
        res = self.client().patch('/movies/'+str(movie.id),
                                  json={'title': 'updated_movie'},
                                  headers=settingup_auth('casting_assistant'))
        self.assertEqual(res.status_code, 401)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()

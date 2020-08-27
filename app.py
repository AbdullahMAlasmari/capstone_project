import os
import sys
from sqlalchemy import exc
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from backend.auth import AuthError, requires_auth
from backend.models import db_drop_and_create_all, setup_db, migrate_db, Movie, Actor, Cast


# def create_app(test_config=None):
    # create and configure the app
app = Flask(__name__)
setup_db(app)
CORS(app)

db_drop_and_create_all()

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
    return response

@app.route('/')
def hello():
    return jsonify({
        'success': True,
        'message': 'Here Are My APIs'
    })

# Movies Endpoints
# @app.route('/movies', methods=['GET'])
# @requires_auth('get:movies')

@app.route('/movies', methods=['GET'])
@requires_auth('get:movies')
def get_all_movie(jwt):
    data = Movie.query.all()
    movie = list(map(Movie.get_movie, data))
    if movie is None or len(movie) == 0:
        abort(404)
    return jsonify({
        'success': True,
        'movie': movie
    })


@app.route('/movies', methods=['POST'])
@requires_auth('post:movies')
# create or add a new movie
def add_movie(payload):

    data = request.get_json()
    
    if not ('title' in data):
        abort(404)

    title = data.get('title', None)
    new_movie_genrs = data.get('movie_genrs', None)
    new_release_date = data.get('release_date', None)

    # i want body to have title, release_date, and movie_genrs
    
    try:
        new_movie = Movie(title=title, release_date=new_release_date, movie_genrs=new_movie_genrs)
        new_movie.insert()
    
        return jsonify({
            'success': True,
            'added': [new_movie.get_movie()]
        })

    except Exception:
        abort(422)

@app.route('/movies/<int:movie_id>', methods=['PATCH'])
@requires_auth('patch:movies')
def update_movies_title(jwt, movie_id):
    movie = Movie.query.filter_by(id=movie_id).first()
    data = request.get_json()

    try:
        title = data.get('title', None)
        movie_genrs = data.get('movie_genrs', None)
        release_date = data.get('release_date', None)

        movie.title = title
        movie.movie_genrs = movie_genrs
        movie.release_date = release_date

        movie.update()

        return jsonify({
            'success': True,
            'edited': movie.id
        }), 200
    
    except(TypeError, KeyError):
        abort(404)
    

# DELETE /movies/:id - Requires delete:movies permission
@app.route('/movies/<int:movie_id>', methods=['DELETE'])
@requires_auth('delete:movies')
def delete_movies(jwt, movie_id):
    movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
    if movie is None:
        abort(404)
    try:
        movie.delete()
    except exc.SQLAlchemyError as error:
        print(error)
        abort(422)

    return jsonify({
        "success": True,
        "deleted": movie.id
    })


# Ends point for Actors
@app.route('/actors', methods=['GET'])
@requires_auth('get:actors')
def getactors(jwt):
    data = Actor.query.all()
    actors = list(map(Actor.get_actor, data))

    # Will cause 404 error if no items on page are found
    if actors is None or len(actors) == 0:
        abort(404)

    return jsonify({
        "success": True,
        'actors': actors
    })

@app.route('/actors/<int:id>', methods=['GET'])
@requires_auth('get:actors')
def get_actor(jwt, id):
    actor = Actor.query.filter(Actor.id == id).one_or_none()
    actor_formatted = actor.short()
    if actor is None:
        abort(404)

    return jsonify({
        "success": True,
        "actor": actor_formatted
    })

@app.route('/actors', methods=['POST'])
@requires_auth('post:actors')
def add_actor(jwt):
    data = request.get_json()

    if data is None:
        abort(404)

    name = data.get('name', None)
    age = data.get('age', None)
    gender = data.get('gender', None)

    # # i want data to have title, release_date, and movie_genrs
    # if name is None or age is None or gender is None:
    #     abort(422)

    try:
        new_actor = Actor(name=name, age=age, gender=gender)
        new_actor.insert()
        return jsonify({
            'success': True,
            'actors': [new_actor.get_actor()]
        })

    except Exception:
        abort(404)

@app.route('/actors/<actor_id>', methods=['PATCH'])
@requires_auth('patch:actors')
def update_actor(jwt, actor_id):

    actor = Actor.query.filter_by(id = actor_id).one_or_none()
    if actor is None:
        abort(404)
    body = request.get_json()
    if body is None:
        abort(404)

    data = request.get_json()
    new_name = data.get('name', None)
    new_age = data.get('age', None)
    new_gender = data.get('gender', None)

    if new_name is not None:
        actor.name = new_name
    if  new_gender is not None:
        actor.gender =  new_gender
    if new_age:
        actor.age = new_age

    try:
        actor.update()
        return jsonify({
            'success': True,
            'edited': [actor.get_actor()]
        })
    except Exception:
        abort(422)

@app.route('/actors/<actor_id>', methods=['DELETE'])
@requires_auth('delete:actors')
def deleteActor(jwt, actor_id):
    actor = Actor.query \
            .filter_by(id=actor_id) \
            .one_or_none()

    if actor is None:
        abort(404)

    try:
        actor.delete()

        return jsonify({
            "success": True,
            "delete": actor_id
        })
    except Exception as e:
        abort(422)
        
# # Ends point for Actor_in_movie it has (movie_id and actor_id)
# @app.route('/casts', methods=['GET'])
# # @requires_auth('get:casts')
# def get_all_cast(payload):
#         data = Cast.query.all()
#         cast = list(map(Cast.get_cast, data))
#         if cast is None or len(cast) == 0:
#             abort(404)
    
#         return jsonify({
#             'success': True,
#             'cast': cast
#             })

# Error Handlers
@app.errorhandler(404)
def page_not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
        }), 404

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "Unauthorized"
        }), 401
        
@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "Bad Request"
        }), 400

@app.errorhandler(500)
def InternalServerError(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "Internal Server Error"
        }), 500

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        'message': 'Unprocessable Entity',
        'success': False
    }), 422

# AuthError defined in auth.py
@app.errorhandler(AuthError)
def authentication(error):
    return jsonify(error.error), 401
    
    # return app

# app = create_app()

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080, debug=True)
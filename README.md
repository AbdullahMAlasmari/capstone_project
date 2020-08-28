# The Casting Agency models
A company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.
# _So let's get started!_

# Installing key Dependencies
## Python 3.8
Follow instructions to install the latest version of python for your platform in the python docs [docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)
## Virtual Enviornment
I recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the python [docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

## PIP Dependecies
- Once you have your venv setup and running, install dependencies by navigating
to the root directory and running:
```bash
   pip3 install -r requirements.txt
```
- This will install all of the required packages included in the requirements.txt file
## Key Dependencies
- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.
- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server
- [Auth0](https://auth0.com/docs/) is the authentication and authorization system we'll use to handle users with different roles with more secure and easy ways
- [Heroku](https://www.heroku.com/what) is the cloud platform used for deployment
- [PostgreSQL](https://www.postgresql.org/) this project is integrated with a popular relational database PostgreSQL, though other relational databases can be used with a little effort

# Local Testing
- To test your local installation, run the following command from the root folder:
```bash
python test_app.py
```
- If all tests pass, your local installation is set up correctly.
# Running the server
- From within the root directory, first ensure you're working with your created
venv. To run the server, execute the following:
```bash
set FLASK_APP=app
set FLASK_DEBUG=true
set FLASK_ENV=development
python app.py
```
## Casting Agency Specifications

### Models

- Movie with attributes title and release date, movie_genrs
- Actor with attributes name, age and gender
- Cast is an association table with attributes actor_id and movie_id

### Endpoints

- GET /actors and /movies
- GET /actors/id and /movies/id
- POST /actors and /movies and
- DELETE /actors/id and /movies/id
- PATCH /actors/id and /movies/id

### Roles
- Executive Producer
  - _All permissions a Casting Director has and_
  - _Add or delete a movie from the database_
- Casting Director
  - _All permissions a Casting Assistant has and_
  - _Add or delete an actor from the database_
  - _Modify actors or movies_
- Casting Assistant
    - _Can view actors and movies_

 ### Tests
- One test for success behavior of each endpoint
- One test for error behavior of each endpoint
- At least two tests of RBAC for each role

#### Auth0 Setup

To set your own auth0 proceed the following steps in [the Doc](https://auth0.com/docs/get-started/learn-the-basics)

 ##### Roles
Establish three roles for users under `Users & Roles` section in Auth0
 Set new API permissions:
    - `get:movies`
    - `post:movies`
    - `patch:movies`
    - `delete:movies`
    - `get:actors`
    - `post:actors`
    - `patch:actors`
    - `delete:actors`

 Set new roles for:
    - Casting Assistant
        - can `get:actors`
        - can `get:movies`
    - Casting Director
        - can perform all Casting Assistant actions
        - can `add:actors`
        - can `delete:actors`
        - can `patch:actors`
        - can `patch:movies`
    - ExecutiveProducer
        - can perform `all actions`
# API Documentation

-   Base URL: https://capstonefs.herokuapp.com/
-   Local Base URL: The local app is hosted at the default http://0.0.0.0:8080/


**Base URL**: Base URL: Actually, this app can be run locally and it is hosted also as a base URL using heroku (the heroku URL is https://capstonefs.herokuapp.com/).

## Error Handling

Errors are returned as JSON object in the following format:
 ```
{
    "success": False,
    "error": 400,
    "message": "Bad Request"
}
```
The API will return three error types when requests fail:

-   400: _Bad Request_
-   401: _Unauthorized_
-   404: _resource not found_
-   422: _Unprocessable Entity_
-   500: _Internal Server Error_

Errors with authentications (401) provide additional info about the error in the form

```
{
    'code': 'authorization_header_missing',
    'description': 'Authorization header is expected.'
}
```
Errors are returned as JSON object in the following format:

```json
{
    "success": False,
    "error": 401,
    "message": ""Unauthorized""
}
```

## Postman

Also, I have included a Postman collection FSND-Capstone.postman_collection.json with each endpoint to make it easy for the reviewer to test. Just change the bearer token to test a different role.

## The movie object

Contains the unique id of the movie, the movie's title, the movie's genre, and the movies release date.

### Example
### GET http://127.0.0.1:5000/movies/1
```
    {
        "id": 1,
        "movie_genrs": "action",
        "release_date": 2020,
        "title": "title"
    }
```
### POST: http://127.0.0.1:5000/movies/7
```
{
  "added": 7,
  "success": true
}
```
### PATCH: http://127.0.0.1:5000/movies/2
```
{
  "edited": 2,
  "success": true
}
```
### DELETE: http://127.0.0.1:5000/movies/7
```
{
  "deleted": 7,
  "success": true
}
```
## The actor object

### GET http://127.0.0.1:5000/actors
```
{
  "actors": [
    {
      "age": 33,
      "gender": "M",
      "id": 1,
      "name": "Alex"
    },
    {
      "age": 61,
      "gender": "M",
      "id": 2,
      "name": " Robert De Niro"
    },
    {
      "age": 71,
      "gender": "M",
      "id": 3,
      "name": "Henry Fonda"
    }
      "name": " Idris Elba"
    },
    "success": true
}
```
### GET: http://127.0.0.1:5000/actors/2
```
{
  "actor": {
    "age": 61,
    "gender": "M",
    "id": 2,
    "name": " Robert De Niro"
  },
  "success": true
}
```
### POST: http://127.0.0.1:5000/actors
```
{
  "added": 5,
  "success": true
}
```

# Heroku Test In postman

### DELETE: https://capstonefs.herokuapp.com/movies/2

### JSON
### Executive Producer'S token:
"........"

```
{
    "movie_genrs": "action",
     "release_date": 2969,
     "title": "Extreme KILLER"
}
```

```

{
    "deleted": 2,
    "success": true
}
```


### GET: https://capstonefs.herokuapp.com/movies
```
{
    "movie": [
        {
            "id": 1,
            "movie_genrs": "action",
            "release_date": 1969,
            "title": "Extreme Measures"
        }
    ],
    "success": true
}
```

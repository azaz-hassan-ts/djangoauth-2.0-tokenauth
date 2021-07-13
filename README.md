# djangoauth-2.0-tokenauth

## Deployed at https://resttokenauth.herokuapp.com/

# Python: Getting Started

A barebones Django app, which can easily be deployed to Heroku.

This application supports the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

## Running Locally

Make sure you have Python 3.9 [installed locally](https://docs.python-guide.org/starting/installation/). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/azaz-hassan-ts/djangoauth.git
$ cd djangoauth

$ python3 -m venv getting-started
$ pip install -r requirements.txt

$ createdb django_auth

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku main

$ heroku run python manage.py migrate
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


## Swagger Documentation Hits


### Got to https://resttokenauth.herokuapp.com/ to see swagger spec document
#### Note: Token Auth is integrated in Swagger Spec document
#### API HIT CYCLE:

```
1. Create a register from swagger link
2. Click on login and send required username and password, it will return a token
3. Now Go on top and click on Authorize and add token in input field "token <token-number>" (without quotes)
4. Now click on profile to view profile info
5. Logout will log you out and won't let you call logout or profile api again with logging in
```

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)



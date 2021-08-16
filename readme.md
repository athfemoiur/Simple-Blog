# Simple Blog with django

Hello everybody, this is a simple blog made with python and Django framework.

 This is my first back-end project with django and it's actually for practice, hope you enjoy :)

## Features
As I said this is a simple blog made with python and django.

In this blog we can easily register then log in

Each post have 3 status ( Published, Draft, Archived ) 

Each user can create a post and have a profile page, we can see our post list or edit our profile through profile page

There is comment and like section for each post

Each post can have one or more categories

Each user can delete and edit the written posts



## Installation

First of all clone the project

```bash
git clone https://github.com/athfemoiur/Simple-Blog.git
```
For this project you need to have postgres-server installed.

First of all use psql to create a new user if you don't have already then create a new database ( remember this information , we need them later)

We need a virtual environment you can create like this : 

```bash
virtualenv venv
```
Then activate it
```bash
source venv/bin/activate
```
Now install all of the packages in requirements.txt file in project directory 
```bash
pip install -r requirements.txt
```
Now You must create local_settings.py file in the project dir and initialize this variables

```python
SECRET_KEY = 'give it a secret key'

DEBUG = True # change it to False for production

DB_NAME = 'the name of the database which you created'
DB_USER = 'the user of the postgres which you created'
DB_PASSWORD = 'the password of that user'
DB_HOST = 'localhost' # can be changed
DB_PORT = 5432 # can be changed

LOCAL_EMAIL_HOST = '
LOCAL_EMAIL_PORT = ''
LOCAL_EMAIL_USE_TLS = True
LOCAL_EMAIL_HOST_USER = ''
LOCAL_EMAIL_HOST_PASSWORD = ''
```
Then you should have a superuser for accessing the admin panel 
```bash
python manage.py createsuperuser
```
Then migrating 
```bash
python manage.py migrate
```
That's finished now you can run the project , I hope so actually :)

```bash
python manage.py runserver
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

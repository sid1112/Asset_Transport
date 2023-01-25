# Asset_Transport

## To run the project

create a virtual environment and run following
pip install django
pip install djangorestframework
pip install mysqlclient
python manage.py makemigrations
python manage.py migrate
django-admin manage.py runserver

## Context

we have a rider and requester. 
A rider can tell which way it is going and how much space it have to carry stuff 
and what time it will reach destination.
A requester can tell how much stuff to carry where to carry and from where to carry and at what date or time.
We have a matching api which requester can use to find out any available rider and then requester can request
for a particular ride.
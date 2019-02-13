1. Create a Procfile
This file is used to explicitly declare your application’s process types and entry points. It is located in the root of your repository.
(requires gunicorn)
You can also specify the tasks to run during release phase p.x.
python manage.py migrate

2. Create a runtime.txt
This will inform heroku for python version


2. pip install django-heroku


3. heroku create
To create a new app. The command’s output shows the app 's name
You do it only once.


4. git push heroku master
pip install -r requirements.txt
python manage.py collectstatic --noinput
launching


5.  heroku run python manage.py migrate
Migrations are not applied by default



# Tips
heroku run python manage.py shell

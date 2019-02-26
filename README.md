# Tutorial

1. Create a Procfile
This file is used to explicitly declare your application’s process types and entry points. It is located in the root of your repository.
(requires gunicorn)
You can also specify the tasks to run during release phase p.x.
python manage.py migrate
include release: bash ./release-tasks.sh
The release-tasks file will have all the release tasks
(dont forget to chmod 0777 release-tasks.sh)

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
You can add it in the release phase (see Procfile)


6. Static files-Templates
Add STATICFILES_DIRS and TEMPLATES-->DIRS in your settings file
heroku runs collectstatic everytime so nothing to add




Creating Different settings (base, dev, production)

1. Create a config folder inside main project folder

2. include __init__.py file

3. create a base.py file and change all paths
basically, is one step up p.x. for Database
os.path.join(os.path.dirname(BASE_DIR), 'db.sqlite3')

4. heroku
a. commit & push changes
b. (dashboard) add config vars DJANGO_SETTINGS_MODULE=mysite.config.production
django_heroku.settings(locals())
This will automatically configure DATABASE_URL, ALLOWED_HOSTS, WhiteNoise (for static assets), Logging, and Heroku CI for your application.

5. locally
a.  export DJANGO_SETTINGS_MODULE=mysite.config.dev
(in wsgi the function setdefault, sets the value only if is empty)


# Tips
heroku run python manage.py shell

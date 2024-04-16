# Setting the Development Environment

## create a virtual environment
```sh
# windows
python -m venv venv

# mac / linux
python3 -m venv venv
```

## activate
```sh
# windows
source ./venv/Scripts/activate

# mac / linux
source ./venv/bin/activate
```

## install django

```sh
pip install django
```

## make project

```sh
django-admin startproject projectName
cd projectName
# run server
python manage.py runserver
```

## Creating App

```sh
python manage.py startapp post
```

## Defining Models

```sh
python manage.py makemigrations
python manage.py migrate
```
specify the project in `settings.py`

```py
INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'post.apps.PostConfig', # our app name
]
```

## create a superuser for our web application that will access the admin panel

not commited

```sh
python manage.py createsuperuser
```

make changes to the `admin.py` file

## Templates

Adding templates folder to `settings.py` file

```py
"DIRS": [BASE_DIR/'templates'],
```




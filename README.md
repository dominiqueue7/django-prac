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


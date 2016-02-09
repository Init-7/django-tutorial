Virtualenv
==========

> virtualenv django-tutorial
> source django-tutorial/bin/activate


Instalacion Django
==================

> pip install django
> python
> > import django
> > django.VERSION


Pip
===

> pip install --upgrade pip
> pip freeze > requirements.txt


Iniciar proyecto Django
=======================

> django-admin startproject tutorial01
> cd tutorial01
> python manage.py runserver


Habilitar Admin
===============

> python manage.py createsuperuser
> python manage.py runserver

http://localhost:8000

> vim [app]/admin.py

from django.contrib import admin
from .models import [Modelname]

admin.site.register([ModelName])



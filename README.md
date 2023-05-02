Charting Library Save/Load Backend
================

This is the tiny backend implementing Charting Library charts storage.

## Requirements
Python 3x, pip, Django, Djongo

## How to start

1. Install Python 3.x and Pip. Use virtual environment if your host has older python version and it cant be upgraded.
2. Install and initialize [mongodb service](https://www.digitalocean.com/community/tutorials/how-to-install-mongodb-on-ubuntu-20-04).
3. Install `mongosh` CLI and check avaliability of database with name 'test'. Create if it's not.
3. Go to your charts storage folder and run `pip install -r requirements.txt`. You need to preinstall `python3-pip` package to do it.
4. Add client.host url from env like at the [connector instructions](https://github.com/doableware/djongo)
5. Run `python3 manage.py migrate`. This will create database schema without any data.
6. Generate a secret key by running `python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`
7. Set your secret key to your environment variables `export SECRET_KEY='...'`
8. Run `python manage.py runserver` to run *TEST* instance of your database. Use some other stuff (i.e., Gunicorn) for your production environment.
9. To run the server in daemon mode use `screen` cli. On next step repeat command from previous step and press `ctrl + a + d` to detach from screen. Process will running in background.

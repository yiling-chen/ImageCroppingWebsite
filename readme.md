# Readme

## Set Up Environment

    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt

## Initialize

    python manage.py migrate
    python manage.py init_data

!! warning !!  
If you do it, all the data will be refresh.  
If you do not want to refresh, just want to load new, use:

    python manage.py load_data


## Run Server

    python manage.py runserver 

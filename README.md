# cxa-query-matchers
Backend for cxa teamtempo office bot project

## Local Configuration Guide

**Ingredients:** python3, django, django rest framework, virtualenv, postgres

    $ cd cxa-query-matchers
    $ virtualenv env
    $ . env/bin/activate
    $ pip install -r requirements.txt
    
    $ cat > .env
    source `dirname ${BASH_SOURCE[0]}`/env/bin/activate
    alias pm="python manage.py"
    export TOKEN=<unknown>

    $ source .env
    $ pm migrate
    $ pm createsuperuser

Then to run the thing:

    $ pm runserver

Runs on http://localhost:8000/

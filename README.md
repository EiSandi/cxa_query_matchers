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

## Heroku Configuration Guide

1. Create app in Heroku
2. Under deploy section, link heroku app to GitHub 
3. To automatically deploy whatever changes made in GitHub, enable automatic deploys. If not, can also deploy manually.
4. Go to Settings and configure environment variable under "Config Variables" Section.


## How to get token?

Run this URL: https://ll-cxa-data.herokuapp.com/token/
Token will be return in json format. 

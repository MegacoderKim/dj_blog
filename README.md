# ![Dj Blog](static/img/python.png)

## Requirements
* Postgres 9.5 - Main datastore

## Installation

1. Clone this repository: `git clone https://github.com/MegacoderKim/dj_blog.git`.
2. `cd` into `jkblog/src/src`: `cd jkblog/src/src`.
3. Install [pyenv](https://github.com/yyuu/pyenv#installation).
4. Install [pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv#installation).
5. Install Python 2.7.13: `pyenv install 2.7.13`.
6. Create a new virtualenv called `jkblog`: `pyenv virtualenv 2.7.13 jkblog`.
7. Set the local virtualenv to `jkblog`: `pyenv local yum_ke`.
8. Reload the `pyenv` environment: `pyenv rehash`. If all went well then your command line prompt should now start with `(jkblog)`.
9. Set up Whoosh indexes `python manage.py rebuild_index`
10. Run the system `python manage.py runserver 0:8000`

## Using Docker (replica of the production system)


1. Install [Docker](https://docs.docker.com/engine/installation/)
2. Run `docker-compose up --build` to build and pull the containters (will take awhile)
3. Set up Whoosh indexes `docker-compose run web python manage.py rebuild_index`


## Coding Conventions/Rules

We try and use the same coding Convenstions as Google.

* Python --> https://google.github.io/styleguide/pyguide.html
* Javascript --> https://google.github.io/styleguide/jsguide.html
* HTML/CSS --> https://google.github.io/styleguide/htmlcssguide.xml

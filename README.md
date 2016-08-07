# Flask Blog

[![Build Status](https://travis-ci.org/juliuskrah/flask-blog.svg?branch=master)](https://travis-ci.org/juliuskrah/flask-blog)
This blog is built using the [Flask](http://flask.pocoo.org/ "Flask Framework") Python microframework.

## Database migration
```shell
$ python db_create.py
```
Creates the database `app.db` and the repository folder structure `db_repository`
```shell
$ pyhton db_migrate.py
```
Migrates database changes and keeps track in `db_repository/versions`
```shell
$ python db_upgrade.py
```
This upgrades your database to the current revision
```shell
$ python db_downgrade.py
```
This downgrades your database to the previous version. This is uncommon in most scenarios
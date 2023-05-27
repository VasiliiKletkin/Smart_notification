# Smart notification ([smartnotification.ru](http://smartnotification.ru/))

This project was created for a specific client according to the ads (listed below).

Project allows you to receive up-to-date information via a link to such sites as:

* [Myhome.ge](https://www.myhome.ge/ka/)
* [SS.ge](https://ss.ge/ka/udzravi-qoneba)

## Stack

* Postgres
* Django
* PytelegramBot
* Rabbit MQ
* Celery

## Start project with `docker-compose`

$ cp .env.example .env.local
$ docker-compose up -d --build

Exec commands for docker containers:

```bash
# load database dump from staging
$ make dcreatedb
$ make dloaddump
# dump database from docker container
$ make dcreatedump
# delete database from docker container
$ make ddeletedb

# make migrations && migrate
$ make dmigr
```

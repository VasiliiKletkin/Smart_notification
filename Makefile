#!make
include .env

run:
	python crm/manage.py runserver
migr:
	python crm/manage.py makemigrations && python crm/manage.py migrate
user:
	python crm/manage.py createsuperuser
req:
	pip freeze > requirements.txt
runbot:
	python bot/main.py

dcollect:
	docker-compose exec web python manage.py collectstatic
dup:
	docker-compose -f "docker-compose.prod.yml" up -d
dupbuild:
	docker-compose -f "docker-compose.prod.yml" up --build
dbuild:
	docker-compose -f "docker-compose.prod.yml" build
dstop:
	docker-compose -f "docker-compose.prod.yml" stop

dmigr:
	docker-compose exec web python manage.py makemigrations && docker-compose exec web python manage.py migrate
duser:
	docker-compose exec web python manage.py createsuperuser
dshell:
	docker-compose exec web python manage.py shell

dcreatedb:
	docker-compose exec postgres createdb -h ${POSTGRES_HOST} -U ${POSTGRES_USER} ${POSTGRES_DATABASE}
ddeletedb:
	docker-compose exec postgres dropdb -h ${POSTGRES_HOST} -U ${POSTGRES_USER} ${POSTGRES_DATABASE}
dloaddump:
	docker-compose exec -T postgres pg_restore --verbose --clean --no-acl --no-owner -h ${POSTGRES_HOST} -U ${POSTGRES_USER} -d ${POSTGRES_DATABASE} < ${POSTGRES_DATABASE}.dump
dcreatedump:
	docker-compose exec postgres pg_dump -Fc --no-acl --no-owner -h ${POSTGRES_HOST} -U ${POSTGRES_USER} ${POSTGRES_DATABASE} > ./${POSTGRES_DATABASE}.dump


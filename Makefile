.PHONY: create-db import-people

# install python deps
install-deps:
	pip install -r requirements.txt

# create database
create-db:
	docker-compose run -T --rm db createdb -h db -U postgres velocity2017

# imports data into database. will create tables if they don't exist
import-people:
	docker-compose run -T -v $(PWD)/assets:/assets --rm db psql -h db -d velocity2017 -U postgres -f /assets/import_people.sql
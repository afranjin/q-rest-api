
.PHONY:
	run-dev
	load-fixtures

run-dev:
	docker-compose -f docker-compose.yml up

load-fixtures:
	docker exec -it q_backend python3 manage.py loaddata users.json
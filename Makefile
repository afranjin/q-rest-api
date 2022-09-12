.PHONY:
	run-dev
	load-data
	add-q-admin
	backend-tests

run-dev:
	docker-compose -f docker-compose.yml up

load-data:
	docker exec -it q_backend python3 manage.py loaddata users.json products.json

add-q-admin:
	docker exec -it q_backend python3 manage.py add_q_admin

backend-tests:
	docker exec -it q_backend pytest
# q-rest-api
### Base project with working interactions between containers:

Docker setup:
- django-drf as `backend`
- postgres as `postgres`

### Setting up development environment

- clone repository `git clone https://github.com/afranjin/q-rest-api.git`
- run `make run-dev`
- After containers up:
    - Add q admin `make add-q-admin`
    - Load initial users / products `make load-data`
- Users: `user_one`, `user_two`, `user_three`, `user_four`, `user_five` -> password: `password`
- Api documentatiton with swager -> http://localhost:8000/swagger/
- Django-admin http://localhost:8000/admin/
- Q - superuser:
    - user: `q-admin`
    - password: `password`
- Tests: `make backend-tests`
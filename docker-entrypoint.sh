#!/bin/sh
python3 -m pip install -r requirements.txt
# Don't run migrations before postgres container running
echo "Waiting for postgres to get up and running..."
while ! nc -z q_db 5432; do
  # where the q_db is the hos, in my case, it is a Docker container.
  echo "waiting for postgress listening..."
  sleep 0.1
done
echo "PostgreSQL started"
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
#!/bin/bash

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py test list

#python3 manage.py runserver

sudo docker build -t  big_pizza .
# sudo docker run -p 8000:8000 big_pizza
git add .

git commmit -m "automate commit"

git push origin main
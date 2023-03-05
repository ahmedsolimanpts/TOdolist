FROM python:3

EXPOSE 3000


COPY . /home/app

WORKDIR /home/app

RUN pip install --upgrade pip

RUN pip install -r requierments.txt

ENTRYPOINT ["python3"]

CMD ["manage.py","runserver","0.0.0.0:8000"]
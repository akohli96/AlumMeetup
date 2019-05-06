FROM python:2.7.16
ENV PYTHONUNBUFFERED 1
WORKDIR /server
COPY requirements.txt /server/
RUN pip install -r requirements.txt
COPY . /server/
EXPOSE 8000
CMD python manage.py makemigrations meetup && python manage.py migrate && python manage.py test && python manage.py loaddata seed.json python manage.py runserver 0.0.0.0:8000

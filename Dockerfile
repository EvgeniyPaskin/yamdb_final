FROM python:3.8.5
WORKDIR /code
COPY . .
RUN pip install -r /code/requirements.txt
# RUN python manage.py collectstatic --noinput
CMD gunicorn yamdb_final.wsgi:application --bind 0.0.0.0:8000
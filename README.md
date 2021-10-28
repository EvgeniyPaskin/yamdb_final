[![Sprint_16 Django-app workflow](https://github.com/EvgeniyPaskin/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)](https://github.com/EvgeniyPaskin/yamdb_final/actions/workflows/yamdb_workflow.yml)

# Описание проекта
Докеризованный проект api_yamdb - платформа по отзывам на произведения культуры

# Клонирование образа c Docker Hub

```
docker push paskin/api_yamdb:v1
```

# Запуск приложения
```
docker-compose up -d --build 
docker-compose exec web python manage.py makemigrations --noinput
docker-compose exec web python manage.py migrate --noinput
docker-compose exec web python manage.py collectstatic --no-input
```

# Создание суперпользователя
..
```
docker-compose exec web python manage.py createsuperuser
```
.....
..
# Наполнение БД начальными данными (фикстуры)

```
docker-compose exec web python manage.py loaddata dump.json
```
..
..

vetr
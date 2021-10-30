[![Sprint_16 Django-app workflow](https://github.com/EvgeniyPaskin/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)](https://github.com/EvgeniyPaskin/yamdb_final/actions/workflows/yamdb_workflow.yml)

# Содержание

1. [Информация про проект](#описание-проекта)
2. [Ссылка на развернутый проект](#ссылка-на-проект)
3. [Установка Docker](#установка-docker)
4. [Клонирование проекта](#клонирование-проекта)
5. [Инструкция по переменным окружения .env](#инструкция-по-заполнению-переменных-окружения)
6. [Команды управления проектом](#команды-управления-проектом)
7. [Используемые технологии](#используемые-технологии)
8. [Текущий статус проекта в Github actions workflow](#статус-проекта)
9. [Информация об авторах](#над-проектом-работали)


## Описание проекта

API_YaMDb – это то REST API сервис, созданный в рамках программы Yandex.Praktikum -> Python Backend Development, который позволяет:
- Cобирать отзывы (Review) пользователей на произведения (Title).
- Вести список категорий (Category) произведений может быть расширен. 
- Присвоить жанр (Genre) произведению из списка предустановленных (новые жанры может создавать  администратор). 
- Пользователям  оставить текстовые отзывы (Review) и 
- Выставлять произведению рейтинг (оценку в диапазоне от одного до десяти). 
- На основании пользовательских рейтингов определять среднюю оценка произведения. 
- Пользователям добавлять комментарии (Comments) к отзывам. 
- За счет кастомной user-модели  назначать различные пользовательские роли (Role).

## Ссылка на проект
Проект развернут благодаря гранту Yandex на облачном сервере Yandex.Cloud и доступен по адресу:

vetrium.ru:
- www.vetrium.ru/admin/
- www.vetrium.ru/api/v1

## Установка Docker
Для запуска контейнирезированного проекта необходим Docker Engine и Docker compose.
Инструкции по установке:

-[Docker Engine](https://docs.docker.com/engine/install/)

-[Docker Compose](https://docs.docker.com/compose/install/)

## Клонирование проекта

Для запуска проекта на компьютере необходимы:
- Python & venv
- Git 
- Docker Engine & Docker Compose
- Telegram bot credentials 

1. Склонируйте репозиторий на локальную машину:
```bash
git clone git@github.com:EvgeniyPaskin/yamdb_final.git
```
Установите и активируйте виртуальное окружение.

Остановите службу ngnix (если запущена).
```bash
sudo systemctl stop nginx 
```

Скопируйте файлы docker-compose.yaml и nginx/default.conf из проекта на сервер в home/<ваш_username>/docker-compose.yaml и home/<ваш_username>/nginx/default.conf соответственно.

Добавьте в Secrets GitHub Actions переменные окружения для работы базы данных и Django в соответствии с [инструкцией](#инструкция-по-заполнению-переменных-окружения)

## Инструкция по заполнению переменных окружения

Переменные окружения ожидаются в .env файле в соответствии с шаблоном [template.env](#https://github.com/EvgeniyPaskin/yamdb_final/blob/master/template.env)

## Команды управления проектом

Запуск проекта:
```bash
docker-compose up -d --build
```

Создание и проведение миграций БД:
```bash
docker-compose exec web python manage.py makemigrations --noinput
docker-compose exec web python manage.py migrate --noinput
```

Сбор статики проекта:
```bash
docker-compose exec web python manage.py collectstatic --no-input
```

Создание суперпользователя:
```bash
docker-compose exec web python manage.py createsuperuser
```

Наполнение БД начальными данными (фикстуры):
```bash
docker-compose exec web python manage.py loaddata dump.json
```

Остановка приложения:
```bash
docker-compose stop
```

## Используемые технологии

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
<img src="https://webassets.mongodb.com/_com_assets/cms/cloud_icon_logo_rgb_2-rbdt1hfuo2.png" width="100" height="28">

## Статус проекта
[![Sprint_16 Django-app workflow](https://github.com/EvgeniyPaskin/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)](https://github.com/EvgeniyPaskin/yamdb_final/actions/workflows/yamdb_workflow.yml)

  
## Над проектом работали

- [Evgeniy Paskin](https://github.com/EvgeniyPaskin)
- [Vladimir Semikin](https://github.com/vsemikin)
- [Nikita Goncharov](https://github.com/EnemoCE)

..............
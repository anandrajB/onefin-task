![ Logo](https://technologies.com/static/media/logo.20c3af3bf8b6aedba1ed0e68ca927882.svg)

#  Django Starter Pack

Welcome to the  Django Starter Pack! This starter pack is designed to help you kickstart your Django projects with some essential configurations and features.


## TECHNOLOGY STACK
[![https://www.python.org/](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![DJANGO](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)](https://www.django-rest-framework.org/)
[![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)](https://heroku.com/)



## Getting Started

Follow these steps to get your project up and running:

### Prerequisites

Make sure you have the following installed on your machine:

- docker
- python
- pip

#### Install docker

https://docs.docker.com/engine/install/

#### Required packages

- [Python](https://www.python.org/downloads/) (3.11 or higher)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [flake8](https://pypi.org/project/flake8/)
- [pylint](https://pypi.org/project/pylint/)

### Clone the Repository

```bash
git clone https://github.com/-tech/_django_starter.git
cd _django_starter
```

### Install required vs code extensions

- Open Visual Studio Code on your local machine.
- Navigate to .devcontainer/devcontainer.json .
- Press Ctrl + P (Windows/Linux) or Cmd + P (Mac) to open the command palette.
- Enter > ***Extensions: Install Extensions*** and press Enter.

### Run via docker

#### do the collecstatic and migrations

```bash
docker-compose run django python manage.py collectstatic
docker-compose run django python manage.py makemigrations
docker-compose run django python manage.py migrate
```

#### create superuser if required

```bash
docker-compose run django python manage.py createsuperuser
```

#### build and run

```bash
docker-compose build
docker-compose up
```

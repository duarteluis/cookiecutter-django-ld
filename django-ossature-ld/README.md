# Ossature de mon projet cookiecutter-django-ld

Structure de base avec les différents éléments de sécurité

## Ajout de paquet django
uv add --package django-ossature-ld <django-package>

## Faire fonctionner le serveur (shell ou server)
uv run --package django-ossature-ld .\manage.py shell

uv run --package django-ossature-ld .\manage.py shell_plus

uv run --package django-ossature-ld .\manage.py runserver 0.0.0.0:8000

## Plugins Django
django-extensions

django-debug-toolbar

## Paramètres pour le Cookiecutter

### .env
- postgres_user
- postgres_password
- postgres_db_name
C'est pour l'url postgres://{{ postgres_user }}:{{ postgres_password }}@127.0.0.1:5432/{{ postgres_db_name }}
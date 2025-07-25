# cookiecutter-django-ld

Template Cookiecutter pour créer rapidement un projet Django structuré et prêt pour la production.

## 🔧 Utilisation

Installe Cookiecutter si nécessaire :

```bash
pip install cookiecutter
```

Puis lance la génération :

```bash
cookiecutter https://github.com/duarteluis/cookiecutter-django-ld.git
```

## ⚙️ Variables configurables

* `project_name` : Nom complet du projet (ex. : "Mon Super Projet")
* `project_slug` : Identifiant du projet (utilisé comme nom de dossier)
* `author_name` : Ton nom ou celui de ton organisation
* `email` : Adresse de contact
* `description` : Brève description du projet
* `use_docker` : "y" ou "n" pour activer le support Docker
* `use_celery` : "y" ou "n" pour activer le support Celery
* `python_version` : Version souhaitée (ex. : "3.12")

## 📦 Stack incluse

* Django
* PostgreSQL (via `psycopg`)
* Celery (optionnel)
* Docker (optionnel)
* Git + pré-configuration `.gitignore`

## 🧪 Tests

Une structure de base pour les tests est incluse avec `pytest` et `pytest-django`.

## 📄 Licence

MIT - © Luis Duarte


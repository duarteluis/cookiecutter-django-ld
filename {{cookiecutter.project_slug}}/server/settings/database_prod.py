# settings/database_prod.py
from .base import BASE_DIR, env

# Parse database connection url strings
# like psql://user:pass@127.0.0.1:8458/db
DATABASES = {
    'default': {
        # read os.environ['DATABASE_URL'] and raises
        # ImproperlyConfigured exception if not found
        #
        # The db() method is an alias for db_url().
        'default': env.db(),
    }
}

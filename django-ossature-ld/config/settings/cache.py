# settings/cache.py
from .base import env

CACHES = {
    "default": env.cache(),
}

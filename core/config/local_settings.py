from .settings import *

DEBUG = True

MIDDLEWARE.append(
    'debug_toolbar.middleware.DebugToolbarMiddleware'
)

INSTALLED_APPS.append(
    'debug_toolbar'
)

INTERNAL_IPS = [
    '127.0.0.1'
]

CSRF_TRUSTED_ORIGINS = ['http://localhost:4200']

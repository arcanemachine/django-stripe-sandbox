from os.path import join as os_path_join

from .helpers import BASE_DIR

"""
* DO NOT DELETE THIS FILE. IT IS REQUIRED FOR LOADING DEFAULTS IN settings.py *
* COPY THIS FILE TO 'local_config.py' IF YOU WISH TO CUSTOMIZE IT. *

This file is for assigning local settings without using environment variables,
or for settings that require Python-specific functionality and thus cannot use
environment variables.

The values here will be used in settings.py if no custom values are assigned.
"""

# important stuff
DJANGO_DEBUG = DEBUG = True
DJANGO_SECRET_KEY = SECRET_KEY =\
    'your_secret_key'
ALLOWED_HOSTS = ['*']

# static files - production server - basic config
# STATIC_ROOT = os_path_join(BASE_DIR, 'staticfiles')
# STATIC_URL = '/staticfiles/'
# STATICFILES_DIRS = [os_path_join(BASE_DIR, 'static')]

# NOTE: the 3 lines below will override the 3 identical variables listed above
# static files - development server - basic config
STATIC_ROOT = None
STATIC_URL = '/static/'
STATICFILES_DIRS = [os_path_join(BASE_DIR, 'static')]

# THIRD-PARTY LIBRARIES #

# stripe
STRIPE_PUBLISHABLE_KEY = 'your_stripe_public_api_key'
STRIPE_SECRET_KEY = 'your_stripe_private_api_key'

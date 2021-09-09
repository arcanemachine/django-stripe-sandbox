import sys

from . import helpers as h, local_config_defaults as defaults

PROJECT_NAME = "Django Stripe Sandbox"
BASE_DIR = h.BASE_DIR


# *********************** BEGIN local config *********************** #
"""
This section contains some values that may differ between servers,
or sensitive content that you don't want committed to source control.

The default values are set to allow for easy deployment.

They may be overridden, and will be checked in the following order:
    - By using an environment variable that starts with 'DJANGO_'.
        - e.g. 'DJANGO_SECRET_KEY'
    - In rate_this_pad/local_config.py
        - An example template may be copied over from local_config.default.py
    - If setting exists in both environment variable and local_config.py,
      then the environment variable will be used.
    - You may also override the settings directly below.
        - However, setting them in local_config.py will prevent any
          sensitive/server-specific information from getting into the repo,
          with no additional effort required on your part.
"""

SHOW_WARNING = True  # set False to disable default config warnings on console

# important stuff
DEBUG = h.get_setting(
    'DEBUG', defaults.DEBUG, bool, SHOW_WARNING)
SECRET_KEY = h.get_setting(
    'SECRET_KEY', defaults.SECRET_KEY, str, SHOW_WARNING)
ALLOWED_HOSTS = h.get_setting(
    'ALLOWED_HOSTS', defaults.ALLOWED_HOSTS, str, False)

# static files
STATIC_ROOT = h.get_setting(
    'STATIC_ROOT', defaults.STATIC_ROOT, bool, False)
STATIC_URL = h.get_setting(
    'STATIC_URL', defaults.STATIC_URL, str, False)
STATICFILES_DIRS = h.get_setting(
    'STATICFILES_DIRS', defaults.STATICFILES_DIRS, list, False)

# THIRD-PARTY LIBRARIES #

# stripe
STRIPE_PUBLISHABLE_KEY = h.get_setting(
    'STRIPE_PUBLISHABLE_KEY', defaults.STRIPE_PUBLISHABLE_KEY, list, True)
STRIPE_SECRET_KEY = h.get_setting(
    'STRIPE_SECRET_KEY', defaults.STRIPE_SECRET_KEY, list, True)

# *********************** END local config *********************** #


AUTH_PW_VALIDATION_PREFIX = 'django.contrib.auth.password_validation'
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': f'{AUTH_PW_VALIDATION_PREFIX}.UserAttributeSimilarityValidator'},
    {'NAME': f'{AUTH_PW_VALIDATION_PREFIX}.MinimumLengthValidator'},
    {'NAME': f'{AUTH_PW_VALIDATION_PREFIX}.CommonPasswordValidator'},
    {'NAME': f'{AUTH_PW_VALIDATION_PREFIX}.NumericPasswordValidator'}]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3'}}

INSTALLED_APPS = ['django.contrib.admin', 'django.contrib.auth',
                  'django.contrib.contenttypes', 'django.contrib.sessions',
                  'django.contrib.messages', 'django.contrib.staticfiles',
                  # local
                  'stripes.apps.StripesConfig',
                  'crispy_forms']

MIDDLEWARE = ['django.middleware.security.SecurityMiddleware',
              'django.contrib.sessions.middleware.SessionMiddleware',
              'django.middleware.common.CommonMiddleware',
              'django.middleware.csrf.CsrfViewMiddleware',
              'django.contrib.auth.middleware.AuthenticationMiddleware',
              'django.contrib.messages.middleware.MessageMiddleware',
              'django.middleware.clickjacking.XFrameOptionsMiddleware']

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': ['templates'],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
            'django_stripe_sandbox.context_processors.context_processors']}}]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LANGUAGE_CODE = 'en-us'
ROOT_URLCONF = 'django_stripe_sandbox.urls'
TIME_ZONE = 'UTC'
USE_I18N = USE_L10N = USE_TZ = True
WSGI_APPLICATION = 'django_stripe_sandbox.wsgi.application'

TESTING = 'test' in sys.argv


# THIRD-PARTY LIBRARIES #

# django-crispy-forms / crispy_forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

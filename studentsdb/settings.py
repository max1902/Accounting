
from django.conf import global_settings

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_CONTEXT_PROCESSORS = \
    global_settings.TEMPLATE_CONTEXT_PROCESSORS + ("django.core.context_processors.request",
 "studentsdb.context_processors.students_proc",
 "students.context_processors.groups_processor",)

PORTAL_URL = 'http://localhost:8000'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sxrwia+gl%n)x+_rlq1&5$whd5si#h2u65mn54d1vrrmavi26$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


ADMIN_EMAIL = 'prokazamax@gmail.com'
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'prokazamax@gmail.com'
EMAIL_HOST_PASSWORD = 'Eae5cYEd1K-6S87juC9e5g'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'contact_form',
    'crispy_forms',
    'students',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'studentsdb.urls'

WSGI_APPLICATION = 'studentsdb.wsgi.application'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

from .db import DATABASES

LANGUAGE_CODE = 'uk'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

import dj_database_url

DATABASES['default'] = dj_database_url.config()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')

try:
    from .db import *
except ImportError:
    pass

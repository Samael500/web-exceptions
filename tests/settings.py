# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

import django

DEBUG = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SITE_ID = 1
SECRET_KEY = "44444444444444444444444444444444444444444444444444"

DATABASES = {}

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "web_exceptions",
]

MIDDLEWARE = (
    'web_exceptions.middleware.WebExceptionsMiddleware',
)

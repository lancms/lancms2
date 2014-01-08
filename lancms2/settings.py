"""
Django settings for lancms2 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z(k&sdwty%-5og5^d4mbj5h+6vylc#o04p0t05!9kevc(#g6+&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',   # for allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'core',
	 'debug_toolbar', # for DEBUG
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'lancms2.urls'

WSGI_APPLICATION = 'lancms2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'lancms2.sql'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Oslo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


#####
MEDIA_ROOT = os.path.join (BASE_DIR, 'media/')
STATIC_ROOT = os.path.join (BASE_DIR, 'static/')
TEMPLATE_DIRS = os.path.join (BASE_DIR, 'templates/')

##### example on how to add to the default settings
# import django.conf.global_settings as DEFAULT_SETTINGS
# TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
# 'django.whatever...',
# )


##### allauth
# plus INSTALLED_APPS

SITE_ID = 1

import django.conf.global_settings as DEFAULT_SETTINGS
TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
	'django.core.context_processors.request',
	'allauth.account.context_processors.account',
	'allauth.socialaccount.context_processors.socialaccount',
	)
AUTHENTICATION_BACKENDS = DEFAULT_SETTINGS.AUTHENTICATION_BACKENDS + (
	'allauth.account.auth_backends.AuthenticationBackend',
	)

SOCIALACCOUNT_PROVIDERS = { 'facebook': { 'SCOPE': ['email'], 'AUTH_PARAMS': { 'auth_type': 'reauthenticate' }, 'METHOD': 'oauth2', 'LOCALE_FUNC': lambda request: 'en_GB' } }

##### end allauth


##### import settings from lancms2/local_settings.py
try:
	from local_settings import *
except ImportError:
	pass


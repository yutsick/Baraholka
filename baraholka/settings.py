"""
Django settings for baraholka project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7p1r-rn6lx$w_a3z=wo-@ezr$h+!xpdv5ms+$iczc!joq-69d1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

AUTH_PROFILE_MODULE = 'www.UserProfile'

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,'templates').
    replace('\\','/'),)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sorl.thumbnail',
    'www',




)

AUTHENTICATION_BACKENDS = (
    'www.backend.EmailAuthBackEnd',
    'django.contrib.auth.backends.ModelBackend',
)

DEFAULT_CHARSET = 'UTF-8'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


)

ROOT_URLCONF = 'baraholka.urls'

WSGI_APPLICATION = 'baraholka.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'baraholka',
        'USER': 'rootadmin',
        'PASSWORD': 'j2G6aaXKqEB42N6f',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')

MEDIA_URL = '/static/media/'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

THUMBNAIL_DEBUG = True
THUMBNAIL_BASEDIR = '/cache/'

STATIC_URL = '/static/'


STATICFILES_DIRS = (
    'static',
    'static/media'
)

FACEBOOK_APP_ID = 1408770569432838
FACEBOOK_REDIRECT_URL = 'http://example.com/login/facebook/'
FACEBOOK_SECRET = '337eb1d914a0e118014065eb6ca81bab'


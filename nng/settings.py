#!/usr/bin/python
# -*- coding: utf-8 -*-

# Django settings for nng project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Haipo Yang', 'yang@haipo.me'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nng',
        'USER': 'nng',
        'PASSWORD': 'nng',
        'HOST': '',                      # Set to empty string for localhost.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-CN'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/home/haipo/nng/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = 'http://media.nng.com/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/home/haipo/nng/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = 'http://static.nng.com/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '+7w9=nzu95v3s&amp;s-)(3=57w21myhc0!hp0g-&amp;9nsyc26ii^zh3'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'accounts.middleware.UserAccountsMiddleware',
)

ROOT_URLCONF = 'nng.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'nng.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/home/haipo/nng/templates'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'avatars',
    'accounts',
    'profiles',
    'messages',
    'data',
    'collect',
    'columns',
    'comments',
    'discusses',
    'domains',
    'dynamic',
    'globalvars',
    'links',
    'remind',
    'shares',
    'topics',
    'votes',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
D_CACHE_AGE = 21600
HOT_TOPICS_CACHE_AGE = 21600
FOLLOWS_CACHE_AGE = 600

INTERNAL_IPS = ('127.0.0.1',)

FOLLOWS_MAX = 200

LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'

AVATARS_DIR = 'avatars'
AVATAR_SMALL_SIZE = 24
AVATAR_SMALL_NAME = 's'
AVATAR_MEDIUM_SIZE = 48
AVATAR_MEDIUM_NAME = 'm'
AVATAR_LARGE_SIZE = 96
AVATAR_LARGE_NAME = 'l'

TAG_AVATAR_ID = -1
TAG_AVATAR_NAME = 'tag.jpg'

USERNAME_RE = r'^[A-Za-z0-9]+$'
NAME_MAX_LEN = 30
SIGNATURE_MAX_LEN = 70
TITLE_MAX_LEN = 300
URL_MAX_LEN = 200

FILTER = False
AVERAGE_TIME = 7
HOT_RATE = 0.8
BOUTIQUE_RATE = 2.0

AUTH_PROFILE_MODULE = 'accounts.UserProfile'
ANONYMOUS_ID = -1
ANONYMOUS_USERNAME = 'anonymous'
ANONYMOUS_PASSWORD = 'anonymous'
ANONYMOUS_NAME = u'匿名用户'
ACCOUNT_CONFIRMED = 'confirmed'
ACCOUNT_CONFIRM_DAYS = 7
ACCOUNT_CONFIRM_FROM_EMAIL = 'nng@nng.com'
CONFIRM_KEY_MAX_LEN = 40

PROFILE_NAME_CHANGE_DAYS = 30

EMAIL_HOST = 'localhost'
EMAIL_PORT = '25'

PASSWORD_LEN_LIMIT = 6

REMEMBER_ME_WEEKS = 2

MESSAGES_PER_PAGE = 30
TAG_FOLLOWS_NUM = 40
COMMENTS_PER_PAGE = 100
MAX_PAGE_NUMBER = 10
COMMENT_DEEPS = 5

WAY_LINK_USER_POST           = 'a'
WAY_LINK_TOPIC_POST          = 'b'
WAY_LINK_DOMAIN_POST         = 'c'
WAY_LINK_SHARE               = 'd'

WAY_DISCUSS_USER_POST        = 'e'
WAY_DISCUSS_TOPIC_POST       = 'f'
WAY_DISCUSS_SHARE            = 'g'

WAY_LINK_COMMENT             = 'h'
WAY_DISCUSS_COMMENT          = 'i'
WAY_LINK_COMMENT_SHARE       = 'j'
WAY_DISCUSS_COMMENT_SHARE    = 'k'


REMIND_NEW_FOLLOWER = 'z'
REMIND_NEW_COMMENT  = 'y'

MAX_TOPICS_NUMBER = 3
LATEST_TOPICS_NUMBER = 30


PREFETCH_RATE = 1.5


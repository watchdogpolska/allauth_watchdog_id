import os
import random
import string
import django

DEBUG = False

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.messages',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth_watchdog_id',
    'tests'
)


# this fixes warnings in django 1.10
MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

if django.VERSION < (1, 10):
    MIDDLEWARE_CLASSES = MIDDLEWARE

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

ROOT_URLCONF = 'allauth.urls'
SITE_ID = 1

SECRET_KEY = ''.join([random.choice(string.ascii_letters) for x in range(40)])

# Database specific

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (
            os.path.join(os.path.dirname(__file__), 'tests', 'templates'),
        ),
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

if django.VERSION < (1, 8):
    TEMPLATE_DIRS = TEMPLATES[0]['DIRS']

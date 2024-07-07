"""
Django settings for orders project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

from dotenv import load_dotenv
import sentry_sdk


ENV_FILENAME = os.getenv('ENV_FILENAME', default='.env')
if ENV_FILENAME is not None and os.path.exists(ENV_FILENAME):
    load_dotenv(ENV_FILENAME)

sentry_sdk.init(
    dsn=os.getenv('SENTRY_DSN'),
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = True if os.getenv('DEBUG').lower() in ("yes", "true", "t", "1") else False

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')

SITE_ID = 1

if DEBUG:
    INTERNAL_IPS = [
        '127.0.0.1',
        'localhost',
    ]

INSTALLED_APPS = [
    'baton',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'drf_spectacular',
    'django_filters',
    'django_rest_passwordreset',
    'social_django',
    'cachalot',
    'backend',
    'baton.autodiscover',
]
if DEBUG:
    INSTALLED_APPS += ['debug_toolbar']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
if DEBUG:
    MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE

ROOT_URLCONF = 'orders.urls'

CSRF_USE_SESSIONS = False  # или True, в зависимости от вашего использования
CSRF_COOKIE_NAME = 'csrftoken'
CSRF_HEADER_NAME = 'HTTP_X_CSRFTOKEN'
CSRF_COOKIE_HTTPONLY = False
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://localhost:1337",
    "http://127.0.0.1:1337",
]
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'orders.wsgi.application'

BATON = {
    'SITE_HEADER': 'Baton Admin Panel',
    'SITE_TITLE': 'Baton Admin Panel',
    'INDEX_TITLE': 'Admin Panel',
    'SUPPORT_HREF': 'https://github.com/otto-torino/django-baton/issues',
    'COPYRIGHT': 'copyright © 2020 <a href="https://www.otto.to.it">Otto srl</a>', # noqa
    'POWERED_BY': '<a href="https://www.otto.to.it">Otto srl</a>',
    'CONFIRM_UNSAVED_CHANGES': True,
    'SHOW_MULTIPART_UPLOADING': True,
    'ENABLE_IMAGES_PREVIEW': True,
    'CHANGELIST_FILTERS_IN_MODAL': True,
    'CHANGELIST_FILTERS_ALWAYS_OPEN': False,
    'CHANGELIST_FILTERS_FORM': True,
    'CHANGEFORM_FIXED_SUBMIT_ROW': True,
    'MENU_ALWAYS_COLLAPSED': False,
    'MENU_TITLE': 'Menu',
    'MESSAGES_TOASTS': False,
    'GRAVATAR_DEFAULT_IMG': 'retro',
    'GRAVATAR_ENABLED': True,
    'LOGIN_SPLASH': '/static/core/img/login-splash.png',
    'CSRF_COOKIE_NAME': 'csrftoken',
    'FORCE_THEME': None,
    'SEARCH_FIELD': {
        'label': 'Search contents...',
        'url': '/search/',
    },
    'BATON_CLIENT_ID': None,
    'BATON_CLIENT_SECRET': None,
    'MENU': (
        {'type': 'app', 'label': 'Images', 'model': 'backend.image'},
        {'type': 'app', 'label': 'Users', 'model': 'backend.user'},
        {'type': 'app', 'label': 'Shops', 'model': 'backend.shop'},
        {'type': 'app', 'label': 'Categories', 'model': 'backend.category'},
        {'type': 'app', 'label': 'Products', 'model': 'backend.product'},
        {'type': 'app', 'label': 'Product Infos', 'model': 'backend.productinfo'},
        {'type': 'app', 'label': 'Parameters', 'model': 'backend.parameter'},
        {'type': 'app', 'label': 'Product Parameters', 'model': 'backend.productparameter'},
        {'type': 'app', 'label': 'Orders', 'model': 'backend.order'},
        {'type': 'app', 'label': 'Order Items', 'model': 'backend.orderitem'},
        {'type': 'app', 'label': 'Contacts', 'model': 'backend.contact'},
        {'type': 'app', 'label': 'Confirm Email Tokens', 'model': 'backend.confirmemailtoken'},
    ),
    'SEARCH_FIELDS': {
        'backend.user': ['email', 'first_name', 'last_name'],
        'backend.shop': ['name'],
        'backend.category': ['name'],
        'backend.product': ['name'],
        'backend.productinfo': ['model', 'external_id'],
        'backend.parameter': ['name'],
        'backend.productparameter': ['value'],
        'backend.order': ['user__email'],
        'backend.orderitem': ['order__user__email', 'product_info__model'],
        'backend.contact': ['user__email'],
        'backend.confirmemailtoken': ['user__email'],
    },
    'MENU_ALWAYS_COLLAPSED': False,
    'CONFIRM_UNSAVED_CHANGES': True,
    'SHOW_MULTIPART_UPLOADING': True,
}

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'NAME': os.getenv('DB_NAME'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'TEST': {
            'NAME': 'orders_test',
        },
    }
}

CELERY_REDIS_DB_HOST = os.getenv('CELERY_REDIS_DB_HOST')
CELERY_REDIS_DB_PORT = os.getenv('CELERY_REDIS_DB_PORT')
CELERY_REDIS_BROKER = os.getenv('CELERY_REDIS_BROKER')

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f"redis://{CELERY_REDIS_DB_HOST}:{CELERY_REDIS_DB_PORT}/{CELERY_REDIS_BROKER}",
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
CACHELOT_BACKEND = 'default'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = os.getenv('TIME_ZONE')

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_PATH = 'static/'
MEDIA_URL = '/media/'
MEDIA_PATH = 'media/'

STATIC_ROOT = os.path.join(BASE_DIR, STATIC_PATH)
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_PATH)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.UserRateThrottle',
        'rest_framework.throttling.AnonRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'user': f'{os.getenv("THROTTLE_RATE_USER_PERMINUTE", default="20")}/minute',
        'anon': f'{os.getenv("THROTTLE_RATE_ANON_PERMINUTE", default="10")}/minute',
    },
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': os.getenv('PAGINATION_PAGE_SIZE', default=100),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

AUTH_USER_MODEL = 'backend.User'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_PORT = 587

CELERY_REDIS_DB_HOST = os.getenv("CELERY_REDIS_DB_HOST")
CELERY_REDIS_DB_PORT = os.getenv("CELERY_REDIS_DB_PORT")
CELERY_REDIS_BACKEND = os.getenv("CELERY_REDIS_BACKEND")
CELERY_REDIS_BROKER = os.getenv("CELERY_REDIS_BROKER")
CELERY_BROKER_URL = f'redis://{CELERY_REDIS_DB_HOST}:{CELERY_REDIS_DB_PORT}/4'
CELERY_RESULT_BACKEND = f'redis://{CELERY_REDIS_DB_HOST}:{CELERY_REDIS_DB_PORT}/2'

SPECTACULAR_SETTINGS = {
    'TITLE': 'Orders Project API',
    'DESCRIPTION': 'Orders',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)
SOCIAL_AUTH_USER_MODEL = 'backend.User'

SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'email',
    'profile',
    'openid'
]

SOCIAL_AUTH_GIHUB_SCOPE = [
    'user'
]

SOCIAL_AUTH_GOOGLE_OAUTH2_ENABLED = True
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')

SOCIAL_AUTH_GITHUB_ENABLED = True
SOCIAL_AUTH_GITHUB_KEY = os.getenv('SOCIAL_AUTH_GITHUB_KEY')
SOCIAL_AUTH_GITHUB_SECRET = os.getenv('SOCIAL_AUTH_GITHUB_SECRET')
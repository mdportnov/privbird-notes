import sys
from os import getenv
from pathlib import Path

from django.utils.translation import gettext_lazy as _
from dotenv import load_dotenv

load_dotenv()

DEBUG = int(getenv('DJANGO_DEBUG', 1))

TEST = len(sys.argv) > 1 and sys.argv[1] == 'test'

DEBUG_PROPAGATE_EXCEPTIONS = True

# Application
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = getenv('DJANGO_SECRET_KEY', 'insecure')

ALLOWED_HOSTS = getenv('DJANGO_ALLOWED_HOSTS', '*').split()

CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:8000',
    'http://localhost:8000',
    'https://127.0.0.1:8000',
    'https://localhost:8000'
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',
    'rest_framework',
    'rosetta',
    'feedbacks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'feedback.urls'

STATIC_ROOT = BASE_DIR / 'static'

STATIC_URL = '/feedback/static/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'static/templates'],
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

WSGI_APPLICATION = 'feedback.wsgi.application'

LOGIN_URL = '/admin/'

# Swagger
SWAGGER_SETTINGS = {
    'DEFAULT_MODEL_RENDERING': 'example'
}

# Cache
REDIS_LOCATION = 'redis://{host}:6379/'.format(
    host=getenv('REDIS_HOST', 'localhost')
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': f'{REDIS_LOCATION}/1',
    }
}

# RestFramework
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'feedback.utils.handlers.exception_handler',
    'DEFAULT_THROTTLE_CLASSES': [
        'feedback.utils.throttle.RateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10/minute' if not TEST else None
    }
}

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': getenv('MARIADB_DATABASE', 'PrivBird'),
        'USER': getenv('MARIADB_USER', 'root'),
        'PASSWORD': getenv('MARIADB_ROOT_PASSWORD', 'realpongo'),
        'PORT': getenv('MARIADB_PORT', '3306'),
        'HOST': getenv('MARIADB_HOST', 'localhost'),
    }
}

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication
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

# Localization
LANGUAGES = (
    ('en', _('English')),
    ('ru', _('Russian'))
)

LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

from os import getenv
from pathlib import Path

from dotenv import find_dotenv, load_dotenv

# Set debug/production mode
load_dotenv(find_dotenv('.env'))

DEBUG = int(getenv('DJANGO_DEBUG', 1))

DEBUG_PROPAGATE_EXCEPTIONS = True

# Load environment depending on mode
load_dotenv(find_dotenv('.env.dev' if DEBUG else '.env.prod'))

# Application
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = getenv('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = getenv('DJANGO_ALLOWED_HOSTS', '*').split()

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',
    'rest_framework',
    'notes',
    'feedbacks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'privbird.urls'

STATIC_ROOT = BASE_DIR / 'static'

STATIC_URL = 'static/'

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

WSGI_APPLICATION = 'privbird.wsgi.application'

# Swagger
SWAGGER_SETTINGS = {
    'DEFAULT_MODEL_RENDERING': 'example'
}

# RestFramework
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'privbird.exceptions.handler.handler'
}

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': getenv('MARIADB_DATABASE', 'PrivBird'),
        'USER': getenv('MARIADB_USER', 'root'),
        'PASSWORD': getenv('MARIADB_ROOT_PASSWORD', 'realpongo'),
        'PORT': getenv('MARIADB_PORT', '3306'),
        'HOST': getenv('DB_HOST', 'localhost'),
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

# Locale
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Celery
CELERY_BROKER_URL = getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')

# Email server configuration
EMAIL_BACKEND = getenv('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_USE_TLS = getenv('EMAIL_USE_TLS', True)
EMAIL_HOST_USER = getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = getenv('EMAIL_HOST_PASSWORD')
EMAIL_HOST = getenv('EMAIL_HOST')
EMAIL_PORT = getenv('EMAIL_PORT')

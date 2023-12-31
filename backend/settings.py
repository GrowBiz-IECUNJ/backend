"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from configparser import ConfigParser
import datetime
import os

# import cloudinary_storage

# Read config file
CONFIG_PATH = Path(os.getcwd()) / "config.ini"
config_parser = ConfigParser()
config_parser.read(CONFIG_PATH)

env = config_parser.get("app", "env")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-0*h)g)h4a0n&$&6+b#3-b7*u-ipwy$+^n^hf&tenafymj0^xxu"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ["growbiz-api.fly.dev"]

ALLOWED_HOSTS = ["*"]

# SIMPLE_JWT: A constant with the expiration of the access and refresh token.
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(days=1),
}

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.template",
    "products",
    "vendor",
    "courses",
    "forum",
    "umkm",
    "wallet",
    "workshop",
    "incubation",
    "user",
    "cloudinary",
    "cloudinary_storage",
    "corsheaders",
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "access-control-allow-origin",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "cache-control",
    "pragma",
]

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)

CSRF_ALLOWED_ORIGINS = ["http://localhost:3000", "http://localhost:8000", "https://growbiz-api.fly.dev"]
CSRF_TRUSTED_ORIGINS = ["http://localhost:8000", "https://growbiz-api.fly.dev"]

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
}

CORS_ORIGIN_ALLOW_ALL = True
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

db_host = config_parser.get("database", "host")
db_port = config_parser.get("database", "port")
db_name = config_parser.get("database", "dbname")
db_user = config_parser.get("database", "user")
db_password = config_parser.get("database", "password")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

if env != "local" and env != "":
    DATABASES["default"] = {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": db_host,
        "PORT": db_port,
        "NAME": db_name,
        "USER": db_user,
        "PASSWORD": db_password,
    }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

for directory in [*STATICFILES_DIRS, STATIC_ROOT]:
    directory.mkdir(exist_ok=True)

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_PROFILE_MODULE = "user.MyUser"

AUTH_USER_MODEL = "user.MyUser"

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": "dnhneesot",
    "API_KEY": "699721619766861",
    "API_SECRET": "XL9QQ3ZY2qgN10mc-Ijww39669k",
}

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

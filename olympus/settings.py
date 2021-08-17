from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

from olympus.config import Config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = Config.SECRET_KEY

DEBUG = Config.DEBUG

ALLOWED_HOSTS = Config.ALLOWED_HOSTS


INSTALLED_APPS = [
    "api",
    "corsheaders",
    "rest_framework",
    "django.contrib.contenttypes",
    "django.contrib.auth",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "olympus.urls"

WSGI_APPLICATION = "olympus.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": Config.DB_NAME,
        "USER": Config.DB_USER,
        "PASSWORD": Config.DB_PASS,
        "HOST": Config.DB_HOST,
    }
}


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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "https://ide.codingminutes.com",
]

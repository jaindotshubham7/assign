import os
import sys
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, "apps"))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    "SECRET_KEY", "09e_rmv0%=q2-d6@1(er!g1c6eq1hn0^hvw8=@k+o4q^t9e_-1"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.staticfiles",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "constance",
    "videos",
    "rest_framework",
    "django_filters",
]

REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "UNAUTHENTICATED_USER": None,
}
MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]
ROOT_URLCONF = "assignment.urls"

CONSTANCE_CONFIG = {
    "searchKeyword": ("ind vs aus", "key word for youtube to search"),
    "limit": (10, "limit"),
}

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

WSGI_APPLICATION = "assignment.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# Database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DBNAME", "fampay"),
        "USER": os.environ.get("POSTGRES_USERNAME", ""),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", ""),
        "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
        "PORT": os.environ.get("POSTGRES_PORT", 5432),
    },
    "redis": {
        "HOST": os.environ.get("REDIS_HOST", "localhost"),
        "PORT": os.environ.get("REDIS_PORT", 6379),
        "DB_INDEX": os.environ.get("REDIS_DB_INDEX", 11),
    },
}

CONSTANCE_REDIS_CONNECTION = {
    "host": DATABASES["redis"]["HOST"],
    "port": DATABASES["redis"]["PORT"],
    "db": 0,
}

CELERY_BROKER_URL = "redis://{host}:{port}".format(
    host=DATABASES["redis"]["HOST"], port=DATABASES["redis"]["PORT"]
)
CELERY_RESULT_BACKEND = "redis://{host}:{port}".format(
    host=DATABASES["redis"]["HOST"], port=DATABASES["redis"]["PORT"]
)

CELERY_BEAT_SCHEDULE = {
    "fetch_latest_video": {
        "task": "videos.tasks.get_latest_video.start_searching_and_adding_youtube_videos",
        "schedule": timedelta(seconds=10),
    },
}

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = False

STATIC_URL = "/staticfiles/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

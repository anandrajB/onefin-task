import os
from datetime import timedelta
from pathlib import Path

import dotenv

from project.database.connection import DATABASE_CONFIG

from .config.logging import LOGGING  # noqa

# --------------#
#  ENV CONFIG   #
# --------------#


BASE_DIR = Path(__file__).resolve().parent.parent
ALLOWED_HOSTS = ["*"]

dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

ALLOWED_HOSTS = ["*"]
DEBUG = True
# -----------------------#
#  IMPORTANT CONFIG - 1  #
# -----------------------#

SECRET_KEY = os.environ.get("SECRET_KEY")

APPEND_SLASH = False
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "drf_yasg",
    "movies_app",
    "rest_framework",
    "rest_framework_simplejwt",
]


ROOT_URLCONF = "project.urls.urls"


# ------------------#
#  TEMPLATE CONFIG  #
# ------------------#


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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


# -----------------------#
#  IMPORTANT CONFIG - 2  #
# -----------------------#


WSGI_APPLICATION = "project.server.wsgi.application"
ASGI_APPLICATION = "project.server.wsgi.application"

# -------------------#
#  DATABASE CONFIG   #
# -------------------#

DATABASES = DATABASE_CONFIG


# ---------------------#
#     AUTHENTICATION   #
# ---------------------#

AUTHENTICATION_BACKENDS = ["django.contrib.auth.backends.ModelBackend"]


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


# ---------------#
#  AUTH SETUP    #
# ---------------#

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
}


# -----------------------#
#  INTERNATIONALIZATION   #
# -----------------------#


LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# -------------------------#
#  STATIC AND MEDIA CONFIG  #
# --------------------------#
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)


# --------------------#
#  MIDDLEWARE CONFIG  #
# --------------------#


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "utils.middleware.RequestCounterMiddleware",
]


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# --------------------#
#  JWT CONFIG  #
# --------------------#

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=6),
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
}

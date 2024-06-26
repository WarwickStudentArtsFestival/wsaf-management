import socket

import environs

env = environs.Env()

"""
Django settings for config project.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

BASE_DIR = environs.Path(__file__).parent.parent.parent  # type: ignore

READ_DOT_ENV_FILE = env.bool("READ_DOT_ENV_FILE", default=True)

if READ_DOT_ENV_FILE is True:
    env.read_env(str(BASE_DIR.joinpath(".env")))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])
INTERNAL_IPS = env.list("INTERNAL_IPS", default=["127.0.0.1"])
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=[])
USE_X_FORWARDED_HOST = env.bool("USE_X_FORWARDED_HOST", default=False)
if USE_X_FORWARDED_HOST is True:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Get the IP to use for Django Debug Toolbar when developing with docker
if env.bool("USE_DOCKER", default=False) is True:
    ip = socket.gethostbyname(socket.gethostname())
    INTERNAL_IPS += [ip[:-1] + "1"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "base",
    "accounts",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # "allauth.socialaccount.providers.github",
    "crispy_forms",
    "crispy_bootstrap5",
    "storages",
    "schedule.apps.ScheduleConfig",
    "maintenance_mode",
    "warwick_sso",
]

MIDDLEWARE = [
    "allauth.account.middleware.AccountMiddleware",
    "django_alive.middleware.healthcheck_bypass_host_check",
    "django.middleware.security.SecurityMiddleware",
    # Whitenoise
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "maintenance_mode.middleware.MaintenanceModeMiddleware",
]

ROOT_URLCONF = "config.urls"

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
                "maintenance_mode.context_processors.maintenance_mode",
                "base.context_processors.site_name",
            ],
        },
    },
]

WSGI_APPLICATION = env("WSGI_APPLICATION", default="config.wsgi.application")
DB_SSL_REQUIRED = env.bool("DB_SSL_REQUIRED", default=False)

# Database
# See https://github.com/jacobian/dj-database-url for more examples
DATABASES = {
    "default": env.dj_db_url(
        "DATABASE_URL", default=f'sqlite:///{BASE_DIR.joinpath("db.sqlite")}', ssl_require=DB_SSL_REQUIRED
    )
}

# Custom User Model
# https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#substituting-a-custom-user-model
AUTH_USER_MODEL = "accounts.User"

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-gb"

TIME_ZONE = "Europe/London"

USE_I18N = True

USE_L10N = True


USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

STORAGES = {
    "default": {
        "BACKEND": env("DEFAULT_FILE_STORAGE", default="django.core.files.storage.FileSystemStorage"),
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        # "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

PUBLIC_ROOT = BASE_DIR.joinpath("public")
STATIC_ROOT = BASE_DIR.joinpath("collected_static")
MEDIA_ROOT = PUBLIC_ROOT.joinpath("media")
PUBLIC_STATIC = PUBLIC_ROOT.joinpath("static")
STATICFILES_DIRS = [str(PUBLIC_STATIC)]
# MEDIA_URL = "/public/media/"
MEDIA_URL = env("WSAF_ASSETS_BASE_URL", "https://assets.wsaf.org.uk") + "/"
STATIC_URL = "/public/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CRISPY-FORMS
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

SITE_ID = 1
SITE_NAME = "WSAF Management"

# DJANGO DEBUG TOOLBAR SETTINGS
if DEBUG is True:
    INSTALLED_APPS += ["debug_toolbar"]
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

# ALLAUTH SETTINGS (https://django-allauth.readthedocs.io/en/latest/configuration.html)
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
LOGIN_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
# This is set to "none" so when trying out an app idea you don't have to have sending emails setup, which can be a pain.
# It's not recommended to leave it as none on a production system. Choose either mandatory or optional.
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False

# CUSTOM Django Base Site ALLAUTH settings used in the custom adapter (apps.accounts.auth_adapter)
ACCOUNT_ADAPTER = "accounts.auth_adapter.AccountAdapter"
ACCOUNT_SIGNUP_OPEN = True
ACCOUNT_SHOW_POST_LOGIN_MESSAGE = False

# See https://github.com/migonzalvar/dj-email-url for more examples on how to set the EMAIL_URL
email = env.dj_email_url(
    "EMAIL_URL",
    default="smtp://skroob@planetspaceball.com:12345@smtp.planetspaceball.com:587/?ssl=True&_default_from_email=President%20Skroob%20%3Cskroob@planetspaceball.com%3E",
)
DEFAULT_FROM_EMAIL = email["DEFAULT_FROM_EMAIL"]
EMAIL_HOST = email["EMAIL_HOST"]
EMAIL_PORT = email["EMAIL_PORT"]
EMAIL_HOST_PASSWORD = email["EMAIL_HOST_PASSWORD"]
EMAIL_HOST_USER = email["EMAIL_HOST_USER"]
EMAIL_USE_TLS = email["EMAIL_USE_TLS"]

DEBUG_LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} - {asctime} - {module} - {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django.request": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": False,
        },
    },
}

PROD_LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {"format": "%(levelname)s - %(asctime)s - %(module)s - %(message)s"},
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django.request": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": False,
        },
    },
}

IS_DEBUG_LOGGING_ON = env.bool("IS_DEBUG_LOGGING_ON", default=False)
LOGGING = PROD_LOGGING

if IS_DEBUG_LOGGING_ON is True:
    LOGGING = DEBUG_LOGGING

# MAINTENANCE MODE SETTINGS
MAINTENANCE_MODE_STATE_BACKEND = "maintenance_mode.backends.CacheBackend"
MAINTENANCE_MODE_STATE_BACKEND_FALLBACK_VALUE = True

VITE_DEV_MODE = env.bool("VITE_DEV_MODE", default=DEBUG)

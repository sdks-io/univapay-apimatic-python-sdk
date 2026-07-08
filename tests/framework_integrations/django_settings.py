# ruff: noqa: D100

SECRET_KEY = "test-secret-key"

DEBUG = True

ALLOWED_HOSTS = [
    "*",
]

ROOT_URLCONF = "tests.framework_integrations.django_urls"

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
]

MIDDLEWARE = []

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": "True",
    },
]

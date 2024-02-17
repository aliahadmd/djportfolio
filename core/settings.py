"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

# dotenv
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-=cldztbc4jg&xl0!x673!*v2_=p$$eu)=7*f#d0#zs$44xx-h^"

# SECURITY WARNING: don't run with debug turned on in production!

# debug true/false with dotenv ->  boolean
DEBUG = True


ALLOWED_HOSTS = [
    "127.0.0.1",
    ".vercel.app",
    "aliahad.com",
    "aliahad.vercel.app",
    ".aliahad.com",
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "portfolio",
    "blog",
    "image",
    "cloudinary",
    "django_summernote",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
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

WSGI_APPLICATION = "core.wsgi.app"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
# Note: Django modules for using databases are not support in serverless
# environments like Vercel. You can use a database over HTTP, hosted elsewhere.

DATABASES = {
    "default": {
        "ENGINE": os.getenv("ENGINE"),
        "NAME": os.getenv(
            "NAME"
        ),  # Replace 'mydatabase' with the name of your PostgreSQL database
        "USER": os.getenv("USER"),  # Replace 'myuser' with your PostgreSQL username
        "PASSWORD": os.getenv(
            "PASSWORD"
        ),  # Replace 'mypassword' with your PostgreSQL password
        "HOST": os.getenv(
            "HOST"
        ),  # Or the hostname where your PostgreSQL server is running
        "PORT": os.getenv(
            "PORT"
        ),  # Or the port number where your PostgreSQL server is listening (usually empty)
    }
}

# django cache feature

# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
#         "LOCATION": "unique-snowflake",  # Can be any unique string
#     }
# }


# Password vimagedation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-vimagedators

AUTH_PASSWORD_VimageDATORS = [
    {
        "NAME": "django.contrib.auth.password_vimagedation.UserAttributeSimilarityVimagedator",
    },
    {
        "NAME": "django.contrib.auth.password_vimagedation.MinimumLengthVimagedator",
    },
    {
        "NAME": "django.contrib.auth.password_vimagedation.CommonPasswordVimagedator",
    },
    {
        "NAME": "django.contrib.auth.password_vimagedation.NumericPasswordVimagedator",
    },
]


# Internationimagezation
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


STATIC_URL = "static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles_build", "static")

# media

# MEDIA_URL = "/media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

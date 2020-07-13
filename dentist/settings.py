"""
Django settings for dentist project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku
import dj_database_url
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0&gn1s!c3!z$w6&m)gjym3_^g*bn3=19wcibzohmdtwh3%=1=y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'dentist.urls'

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
                'django_settings_export.settings_export',
                
            ],
        },
    },
]


WSGI_APPLICATION = 'dentist.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Email settings using localhost smpt server
# ---------------------------------
# Command for activate localhost smpt server
# python -m smtpd -n -c DebuggingServer localhost:1025

# Email settings using Python Localhost
# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 1025
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_USE_TLS = False
# ---------------------------------END


# Email settings using Google Smtp
# ---------------------------------
# option-1
# myaccount.google.com/lesssecureapps
# accounts.google.com/DisplayUnlockCaptcha
# ---------------------------------
# option-2
# myaccount.google.com/apppasswords
# ---------------------------------
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'rabbanii.testsmtp@gmail.com'
EMAIL_HOST_PASSWORD = 'fgoendrwzvzbiuat'
EMAIL_USE_TLS = True
# ---------------------------------EN


django_heroku.settings(locals())




BUSINESS_NAME = 'Dental World';
BUSINESS_EMAIL = 'info@dentalworld.com';
BUSINESS_ADDRESS = 'Hous#01 Road#12 Sector#22 Uttara, Dhaka 1230, Bangladesh.';
BUSINESS_PHONE = '01700-000000';
BUSINESS_FAX = '-';
BUSINESS_MESSAGE = 'Bonding is a fast and painless treatment that can create a youthful, healthy smile and a better first impression. A simple bonding can be done in a single visit for noticeable smile improvement. Ask us if you can improve your smile with bonding!';

GOOGLE_MAP = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3648.651055059057!2d90.38935626885296!3d23.8665216827023!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3755c4197a8d8b49%3A0xd853bcc1eace97e9!2zMjPCsDUxJzU4LjciTiA5MMKwMjMnMjIuMiJF!5e0!3m2!1sen!2sbd!4v1593512996597!5m2!1sen!2sbd';

FACEBOOK_LINK = 'https://www.facebook.com/Sochetonota/';
TWITTER_LINK = '#';
GOOGLE_PLUS_LINK = '#';
LINKEDIN_LINK = 'https://www.linkedin.com/in/mkrabbani/';
PINTEREST_LINK = '#';


DAY_1_NAME = 'Friday';
DAY_2_NAME = 'Saturday';
DAY_3_NAME = 'Sunday';
DAY_4_NAME = 'Monday';
DAY_5_NAME = 'Tuesday';
DAY_6_NAME = 'Wednessday';
DAY_7_NAME = 'Thursday';
DAY_1_OPENING_TIME = '09.00 AM - 22.00 PM';
DAY_2_OPENING_TIME = '09.00 AM - 22.00 PM';
DAY_3_OPENING_TIME = '09.00 AM - 22.00 PM';
DAY_4_OPENING_TIME = '09.00 AM - 22.00 PM';
DAY_5_OPENING_TIME = '09.00 AM - 22.00 PM';
DAY_6_OPENING_TIME = '09.00 AM - 22.00 PM';
DAY_7_OPENING_TIME = 'Closed';

ABOUT_US_TEXT = 'Dental World invites you as a patient! We utilize the most recent dental innovation to offer incredible dental consideration to give a charming, calm ordeal. For your benefit, our clinics offer nighttimes and Saturday arrangements just as electronic protection preparing for simple and fast installment. Our theory for our clinics is the thing that we take a stab at ordinary. “A family situated practice in an amicable and minding condition devoted to brilliance.” We anticipate making cheerful, solid and splendid grins for you and your family in the years ahead.'



SETTINGS_EXPORT = [
    'BUSINESS_NAME',
    'BUSINESS_EMAIL',
    'BUSINESS_ADDRESS',
    'BUSINESS_PHONE',
    'BUSINESS_FAX',
    'BUSINESS_MESSAGE',
    
    'GOOGLE_MAP',

    'FACEBOOK_LINK',
    'TWITTER_LINK',
    'GOOGLE_PLUS_LINK',
    'LINKEDIN_LINK',
    'PINTEREST_LINK',

    'DAY_1_NAME',
    'DAY_2_NAME',
    'DAY_3_NAME',
    'DAY_4_NAME',
    'DAY_5_NAME',
    'DAY_6_NAME',
    'DAY_7_NAME',
    'DAY_1_OPENING_TIME',
    'DAY_2_OPENING_TIME',
    'DAY_3_OPENING_TIME',
    'DAY_4_OPENING_TIME',
    'DAY_5_OPENING_TIME',
    'DAY_6_OPENING_TIME',
    'DAY_7_OPENING_TIME',

    'ABOUT_US_TEXT',
]



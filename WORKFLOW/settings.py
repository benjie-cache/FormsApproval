"""
Django settings for WORKFLOW project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from asyncio.sslproto import SSLProtocol
from pathlib import Path
import os
import mimetypes
from smtplib import SMTP_SSL
mimetypes.add_type("text/css", ".css", True)
import ldap
from django_auth_ldap.config import LDAPSearch,logging

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =True
ALLOWED_HOSTS = ['*','localhost','127.0.0.1','VIRTUAL.kws.local','172.16.4.160','192.168.173.1']
#SESSION_COOKIE_SECURE=True
#CSRF_COOKIE_SECURE=True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'access',
    'core',
     'blacklist',
    'email_form',
    'viewflow',
    'crispy_forms',
    'newusersunsystem',
   # 'allauth',
   #'allauth.account',
   # 'allauth.socialaccount',
    'rest_framework'
  
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
     'blacklist.middleware.BlacklistMiddleware',
]

ROOT_URLCONF = 'WORKFLOW.urls'
import django
if django.VERSION < (1, 10):
    MIDDLEWARE_CLASSES = MIDDLEWARE
AUTH_USER_MODEL = 'accounts.User'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
        os.path.join(BASE_DIR, 'templates/access'),
        os.path.join(BASE_DIR, 'templates/accounts'),
        os.path.join(BASE_DIR, 'templates/access/rms_application'),
         os.path.join(BASE_DIR, 'templates/email_form/emailrequest'),
          os.path.join(BASE_DIR, 'templates/newusersunsystem/newusersunsystem'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                 'core.context_processors.tasks_counts',
                  'core.context_processors.resolver_context_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'WORKFLOW.wsgi.application'


DATABASES = {
   'default':  {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'form_access_db',
       'USER': 'postgres',
       'PASSWORD':os.environ['DATABASE_PASSWORD'],
       'HOST': '127.0.0.1',
       'PORT': 5432,

   }
}
CRISPY_TEMPLATE_PACK = 'bootstrap4'
AUTHENTICATION_BACKENDS = [
    'django_auth_ldap.backend.LDAPBackend',
  'django.contrib.auth.backends.ModelBackend',
    #'allauth.account.auth_backends.AuthenticationBackend',
]

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT=os.path.join(BASE_DIR,'static')
#STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),os.path.join(BASE_DIR, 'static/assets/bootstrap')]
COLLECTSTATIC=1

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGOUT_REDIRECT_URL = '/accounts/login/' 
LOGIN_REDIRECT_URL = 'dashboard'


#LOGIN_ATTEMPTS=3
#ACCOUNT_FORMS={
   # 'signup':'accounts.forms.CustomSignUpForm'
#}



AUTH_LDAP_SERVER_URI ='ldap://172.16.1.2:3268'
AUTH_LDAP_ALWAYS_UPDATE_USER = True
AUTH_LDAP_BIND_DN = "ldapauth@KWS.local"
AUTH_LDAP_BIND_PASSWORD ='w!ldl!f3y3tu'

AUTH_LDAP_USER_SEARCH = LDAPSearch(
    "dc=KWS,dc=local", ldap.SCOPE_SUBTREE,"sAMAccountName=%(user)s"
)


AUTH_LDAP_USER_ATTR_MAP = {
"username": "sAMAccountName",
"password": "userPassword"
}
AUTH_LDAP_USER_ATTR_MAP = {
    
    "username": "sAMAccountName",
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "loggers": {"django_auth_ldap": {"level": "DEBUG", "handlers": ["console"]}},
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.kws.org'
EMAIL_PORT=587
EMAIL_HOST_USER = 'kws\ithelpdesk'
EMAIL_HOST_PASSWORD = 'Helpdesk321@pop'


EMAIL_USE_TLS= True

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
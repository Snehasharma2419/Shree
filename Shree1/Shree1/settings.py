import os
from pathlib import Path

# 1. Paths
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Security
SECRET_KEY = 'django-insecure-shree-internal-key'
DEBUG = True
ALLOWED_HOSTS = []

# 3. App Definition
INSTALLED_APPS = [
    'django.contrib.admin',        # Required for admin.site.urls
    'django.contrib.auth',         # Required for admin and login
    'django.contrib.contenttypes', # Required for permissions
    'django.contrib.sessions',     # Required for login and language
    'django.contrib.messages',     # Required for admin notifications
    'django.contrib.staticfiles',  # Required for CSS/JS
    'Shree1',                      # Your main app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Must be before LocaleMiddleware
    'django.middleware.locale.LocaleMiddleware',             # For Language Change
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Required for Admin
    'django.contrib.messages.middleware.MessageMiddleware',      # Required for Admin
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Shree1.urls'

# 4. Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'template'], #
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',      # Required for Admin
                'django.contrib.messages.context_processors.messages', # Required for Admin
            ],
        },
    },
]

WSGI_APPLICATION = 'Shree1.wsgi.application'

# 5. Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 6. Static Files
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static', #
]

# 7. Internationalization (Language Change)
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('en', 'English'),
    ('hi', 'Hindi'),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
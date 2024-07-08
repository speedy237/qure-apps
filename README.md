# QureAPI

QureAPI est une API RESTful construite avec Django et Django REST Framework. Elle permet de gérer des consultations médicales, des patients, des praticiens et des organisations.

## Prérequis

- Python 3.11.5
- pip
- Git
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

## Installation locale

1. Clonez le dépôt :

    ```sh
    git clone  https://github.com/speedy237/qure-apps.git
    cd qure-apps
    ```

2. Créez un environnement virtuel nommé `qure` et activez-le :

    ```sh
    python -m venv qure
    source qure/bin/activate  # Sur Windows: qure\Scripts\activate
    ```

3. Installez les dépendances :

    ```sh
    pip install -r requirements.txt
    ```

4. Configurez la base de données PostgreSQL locale dans `settings.py` :

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'quredb',
            'USER': 'qureadmin',
            'PASSWORD': '@Qwerty123!',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

5. Appliquez les migrations et démarrez le serveur de développement :

    ```sh
    python manage.py migrate
    python manage.py runserver
    ```

6. Accédez à l'API à l'adresse [http://localhost:8000](http://localhost:8000).

## Déploiement sur Heroku

1. Connectez-vous à Heroku et créez une nouvelle application :

    ```sh
    heroku login
    heroku create your-app-name
    ```

2. Ajoutez PostgreSQL à votre application Heroku :

    ```sh
    heroku addons:create heroku-postgresql:hobby-dev
    ```

3. Configurez les variables d'environnement :

    ```sh
    heroku config:set DJANGO_SECRET_KEY='your-secret-key'
    heroku config:set DJANGO_DEBUG=False
    ```

4. Déployez l'application sur Heroku :

    ```sh
    git push heroku main
    ```

5. Appliquez les migrations et collectez les fichiers statiques :

    ```sh
    heroku run python manage.py migrate
    heroku run python manage.py collectstatic --noinput
    ```

6. Ouvrez l'application dans votre navigateur :

    ```sh
    heroku open
    ```

## Configuration des fichiers

### `settings.py`

```python
import dj_database_url
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-i)h_z0pb+!!@bz=&zt-d7dq+q5mcxe*azx-3tj%a$5ma&sn2kc')

DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'

ALLOWED_HOSTS = ['your-heroku-app-name.herokuapp.com', 'localhost', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'qure2'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'qureapi.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'qureapi.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

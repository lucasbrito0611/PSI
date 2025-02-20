from .settings import*

DEBUG = True

SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbpsi',
        'USER': 'dbpsi_owner',
        'PASSWORD': 'npg_sSPlDnTd4L0K',
        'HOST': 'ep-restless-fog-a8zfr0gh-pooler.eastus2.azure.neon.tech',
        'PORT': '5432',
        'OPTIONS': {'sslmode': 'require'},
    }
}
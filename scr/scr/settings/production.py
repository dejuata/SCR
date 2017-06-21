from unipath import Path
from .base import *
import os


DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': 'scrdbprod',
        'USER': 'scruserprod',
        'PASSWORD': 'america27',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

AWS_STORAGE_BUCKET_NAME = 'scrvistas'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = 'AKIAJ3GVEFT32KLMEBJA'
AWS_SECRET_ACCESS_KEY = '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'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = 'https://s3.amazonaws.com/scrvistas/'
MEDIA_URL = 'https://s3.amazonaws.com/scrvistas/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
#STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static_collected')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

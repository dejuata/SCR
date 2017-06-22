import os
from django.core.urlresolvers import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from unipath import Path

BASE_DIR = Path(__file__).ancestor(3)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '--vbdj4q63g3#=36p6i5!5alpsrle7qvil_*=(0z(a7os^a0c&'

# django_tenants
ADMINS = (
    ('dejuata', 'dejuata@hotmail.com'),
)

MANAGERS = ADMINS

SHARED_APPS = (
    'django_tenants',
    'apps.tenant',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'custom_user',
    'apps.users',
    'apps.custom_admin',
    'snowpenguin.django.recaptcha2',
    'anymail',
    'apps.cities',
    'django_select2',
    'turbolinks',
    'social_django',
)

TENANT_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.messages',
    'apps.users',
    'apps.cliente',
    'apps.conductor',
    'apps.vehiculo',
    'apps.ruta',
    'apps.planilla',
    'apps.custom_ui',
    'apps.data_json',
)

INSTALLED_APPS = list(set(SHARED_APPS + TENANT_APPS))

TENANT_MODEL = "tenant.Tenant"  # app.Model
TENANT_DOMAIN_MODEL = "tenant.Domain"

MIDDLEWARE = [
    'django_tenants.middleware.TenantMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'turbolinks.middleware.TurbolinksMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'scr.tenant_urls'
PUBLIC_SCHEMA_URLCONF = 'scr.public_urls'

PUBLIC_SCHEMA_NAME = 'public'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

# ------------------------- AUTH -------------------------#

AUTH_USER_MODEL = 'users.MyCustomEmailUser'
SOCIAL_AUTH_USER_MODEL = 'users.MyCustomEmailUser'

# User login
LOGIN_URL = 'tenant_login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = reverse_lazy('index')
LOGOUT_REDIRECT_URL = reverse_lazy('index')

SOCIAL_AUTH_LOGIN_REDIRECT_URL = reverse_lazy('index')
SOCIAL_AUTH_LOGIN_ERROR_URL = reverse_lazy('index')
SOCIAL_AUTH_RAISE_EXCEPTIONS = False

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GoogleOAuth',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',

    # Make up a username for this person, appends a random string at the end if
    # there's any collision.
    # 'social_core.pipeline.user.get_username',

    # CUSTOM: this gets email address as the username and validates it matches
    # the logged in user's email address.
    'apps.users.pipeline.get_username',

    # 'social_core.pipeline.mail.mail_validation',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details'
)

# secrets id auth social
SOCIAL_AUTH_TWITTER_KEY = 'rIcFcMVUbegQWPvPNY3Q2VKZV'
SOCIAL_AUTH_TWITTER_SECRET = 'Mmz23dk0YYQA7naoShV1PZ5Vl0m7OQM3q5PcuQaJkkHitgYL6X'
SOCIAL_AUTH_TWITTER_SCOPE = ['email']
SOCIAL_AUTH_TWITTER_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, email',
}

SOCIAL_AUTH_FACEBOOK_KEY = '910029992471998'
SOCIAL_AUTH_FACEBOOK_SECRET = 'baa05f0adbb33fd858443e58539c33a9'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email',
}

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '128173655574-7fecombl7flt0ivnsi6opdrkgcqiiil3.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '7IqdD0ULO9l9Ei1u18i5PgJ8'

# ------------------------- END AUTH -------------------------#

WSGI_APPLICATION = 'scr.wsgi.application'

DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Django JET

JET_DEFAULT_THEME = 'default'
JET_THEMES = [
    {
        'theme': 'default',
        'color': '#47bac1',
        'title': 'Default'
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]

# JET_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'
# JET_APP_INDEX_DASHBOARD = 'dashboard.CustomAppIndexDashboard'

JET_SIDE_MENU_COMPACT = True

# django-recapchat
RECAPTCHA_PUBLIC_KEY = '6Lc_RB4UAAAAAIjVIJgONuqnMd3sVRZwLEVC_rvH'
RECAPTCHA_PRIVATE_KEY = '6Lc_RB4UAAAAALGWluRsX4qP3TKNy-sw3eUFCYpd'

# RECAPTCHA_PROXY = 'http://127.0.0.1:8000'


# django_tenants
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Email transactional anymail
ANYMAIL = {
    # (exact settings here depend on your ESP...)
    "MAILGUN_API_KEY": "key-c91e693c95ab9d0ade486c8b5cc1cde6",
    "MAILGUN_SENDER_DOMAIN": 'juandavidpino.com',  # your Mailgun domain, if needed
}
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"  # or sendgrid.EmailBackend, or...
DEFAULT_FROM_EMAIL = "juan.david.pino.reyes@gmail.com"  # if you don't already have this in settings

# django-excel
FILE_UPLOAD_HANDLERS = ("django_excel.ExcelMemoryFileUploadHandler",
                        "django_excel.TemporaryExcelFileUploadHandler")

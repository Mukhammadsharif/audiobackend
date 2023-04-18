DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd1auq1j765a3vk',
        'USER': 'plfrkschaulvqp',
        'PASSWORD': 'ffad9700ee1e10f3fea85fa9ecdf14cedd17d3f9cee1757a161bdc2f3f909b74',
        'HOST': 'ec2-52-73-155-171.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

BACKEND_DOMAIN = ''
FRONTEND_DOMAIN = ''

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mymoodlab@gmail.com'
EMAIL_HOST_PASSWORD = 'musurbekmsh2747424'
SERVER_EMAIL = EMAIL_HOST_USER
EMAIL_USE_TLS = True


ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'mymoodlab@gmail.com'
ACCOUNT_EMAIL_VERIFICATION = 'mymoodlab@gmail.com'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/?verification=1'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/?verification=1'

SITE_ID = 1
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

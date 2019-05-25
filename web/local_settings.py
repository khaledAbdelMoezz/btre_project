

SECRET_KEY = 'gfrr&3y!$(%jg38_s!o#q)kmb$-9u$u6atyc003!6u$hv%qvm_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['165.22.84.214']






DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'webdb',
        'USER':'dbadmin',
        'PASSWORD':'safi0303',
        'HOST':'localhost',
    }
}



EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER ='khaled.a.moezz@gmail.com'
EMAIL_HOST_PASSWORD ='Safi0303%'     #  should get a password
EMAIL_USE_TLS = True

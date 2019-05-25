

SECRET_KEY = 'gfrr&3y!$(%jg38_s!o#q)kmb$-9u$u6atyc003!6u$hv%qvm_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['IP']






DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '********',
        'USER':'*******',
        'PASSWORD':'******',
        'HOST':'localhost',
    }
}



EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER ='xxxxxx@gmail.com'
EMAIL_HOST_PASSWORD ='*********'     #  should get a password
EMAIL_USE_TLS = True

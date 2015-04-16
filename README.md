# Location Service

This is a service for registering, storing and retrieving location information for use by 
dashboards and other services through APIs

# Setup

- `pip install -r requirements.txt`
- create dev database user `createuser onadev --interactive`
- Create a local_settings file in the onalocation/settings with the following:
```python
    from .base import *  # noqa


    DEBUG = True
    TEMPLATE_DEBUG = True

    # Database
    # https://docs.djangoproject.com/en/1.8/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'onalocation',
            'USER': 'onadev',
            'PASSWORD': 'on@d3v',
            'HOST': '127.0.0.1',
        }
    }
```
- set the `onadev` user password in psql through:
    + `postgres=# alter user "onadev" with password 'on@d3v';`
- `./manage syncdb`
- `./manage migrate`

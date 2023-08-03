from edroh_blog.settings.base import *



LOCAL_APPS=[
    "posts",
    "apis",
    "accounts",
    "essayexpert"
    ]
FRAMEWORKS=['rest_framework',]

INSTALLED_APPS +=LOCAL_APPS
INSTALLED_APPS +=FRAMEWORKS

#  REST FRAMEWORK SETTINGS



REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication"
    ],
}




CORS_ALLOW_ALL_ORIGINS=True




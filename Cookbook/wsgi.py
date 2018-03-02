"""
WSGI config for Cookbook project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
from whitenoise.django import DjangoWhiteNoise
from django.core.wsgi import get_wsgi_application
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'Cookbook.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Cookbook.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)

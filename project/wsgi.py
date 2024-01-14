"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""
import os
import django
from pathlib import Path
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

BASE_DIR = Path(__file__).resolve().parent.parent

# Call django.setup once
django.setup(set_prefix=False)

application = get_wsgi_application()
application = WhiteNoise(application, root=os.path.join(BASE_DIR, "staticfiles"))

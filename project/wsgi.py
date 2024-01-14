"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""
import os
from pathlib import Path
from whitenoise import WhiteNoise
BASE_DIR = Path(__file__).resolve().parent.parent

from project import MyWSGIApp

application = MyWSGIApp()
application = WhiteNoise(application, root=os.path.join(BASE_DIR, "staticfiles"))


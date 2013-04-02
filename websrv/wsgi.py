#!/usr/bin/env python

import sys
import os
import os.path

activate_this = '/home/webmaster/venv/try/django-settings/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

PARENT_PRJ_PATH = '/home/webmaster/venv/try/django-settings/'
PRJ_PATH = os.path.join(PARENT_PRJ_PATH, "mysite")
PRJ_APPS = [ "polls", ]

#sys.path.append(PARENT_PRJ_PATH)
sys.path.append(PRJ_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from websrv import monitor
import django.core.handlers.wsgi

def list_files(arg, dirname, names):
    for entry in names:
        if entry[-1] == "~" or entry[-3:-1] == "pyc":
            continue
        else:
            monitor.track(os.path.join(arg, entry))

monitor.start(interval=1.0)
for app in PRJ_APPS:
    path = os.path.join(PRJ_PATH, app)
    os.path.walk(path, list_files, path)

application = django.core.handlers.wsgi.WSGIHandler()

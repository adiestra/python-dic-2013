"""
WSGI config for proyecto1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proyecto1.settings")


ROOT_DIR = os.path.realpath(
  os.path.join(
    os.path.dirname(__file__),
    '../../'
  )
)

VENV_DIR = '%s/env' % ROOT_DIR

activate_this_file = "%s/bin/activate_this.py" % VENV_DIR

#print activate_this_file

PROJECT_DIR = os.path.realpath(
  os.path.join(
    os.path.dirname(__file__),
    '../'
  )
)

sys.path.insert(0, PROJECT_DIR)
#print sys.path
#sys.exit()

execfile(
    activate_this_file,
    dict(__file__=activate_this_file)
)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

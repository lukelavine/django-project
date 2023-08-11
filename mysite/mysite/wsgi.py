"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import site
import sys

from django.core.wsgi import get_wsgi_application

site.addsitedir('/home/ubuntu/django/webenv/lib/python3.9/site-packages')

sys.path.append('/home/ubuntu/django/mysite')
sys.path.append('/home/ubuntu/django/mysite/mysite')

os.environ['DJANGO_SETTINGS_MODULE'] =  'mysite.settings'

activate_env=os.path.expanduser('/home/ubuntu/django/webenv/bin/activate_this.py')
exec(open(activate_env).read(), {'__file__': activate_env})

application = get_wsgi_application()

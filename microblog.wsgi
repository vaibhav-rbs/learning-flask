#!/usr/bin/python
import os
import logging
import sys

activate_this = '/var/www/microblog/flask/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/microblog")

from app import app as application
application.secret_key = "E=MC^2"

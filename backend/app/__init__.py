__author__ = 'mwn'

import os
import sys
import logging

from logging.handlers import RotatingFileHandler
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('settings')
handler = RotatingFileHandler('yapki.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.DEBUG)
app.logger.addHandler(handler)


########################
# Configure Secret Key #
########################
def install_secret_key(app, filename='secret_key'):
    """Configure the SECRET_KEY from a file
    in the instance directory.

    If the file does not exist, print instructions
    to create it from a shell with a random key,
    then exit.
    """
    filename = os.path.join(app.instance_path, filename)

    try:
        app.config['SECRET_KEY'] = open(filename, 'rb').read()
    except IOError:
        print('Error: No secret key. Create it with:')
        full_path = os.path.dirname(filename)
        if not os.path.isdir(full_path):
            print('mkdir -p {filename}'.format(filename=full_path))
        print('head -c 24 /dev/urandom > {filename}'.format(filename=filename))
        sys.exit(1)

if not app.config['DEBUG']:
    install_secret_key(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.after_request
def after_request(response):
    response.headers.add('X-Test', 'This is only test.')
    response.headers.add('Access-Control-Allow-Origin', '*')  # TODO: set to real origin
    return response

from app.web.controller import webBp
app.register_blueprint(webBp)
from app.rest.controller import restBp
app.register_blueprint(restBp)

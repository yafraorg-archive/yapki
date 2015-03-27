# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# (c) yafra.org, 2002, Switzerland
#
#-------------------------------------------------------------------------------
#
# python eve run.py

import os
import imp

database = imp.load_source('database', 'database.py')
import json
#from eve import Eve
from flask import Flask
from flask import jsonify
from database import Database
import logging
from logging.handlers import RotatingFileHandler


# Heroku support: bind to PORT if defined, otherwise default to 5000.
if 'PORT' in os.environ:
    port = int(os.environ.get('PORT'))
    # use '0.0.0.0' to ensure your REST API is reachable from all your
    # network (and not only your computer).
    host = '0.0.0.0'
else:
    port = 8080
    host = '0.0.0.0'

#app = Eve()
app = Flask("yapki")


@app.route("/db")
def DbPage():
    app.logger.info('start db list get')
    myDb = Database()
    indexContent = myDb.certlist("/data/pki/yapki/index.txt")
    app.logger.debug(indexContent)
    json_data = json.dumps(indexContent)
    app.logger.debug(json_data)
    return jsonify(json_data)


@app.route("/info")
def InfoPage():
    return jsonify(version='1.0.1',
                   status='OK')


@app.after_request
def after_request(response):
    response.headers.add('X-Test', 'This is only test.')
    response.headers.add('Access-Control-Allow-Origin', '*')  # TODO: set to real origin
    return response


if __name__ == '__main__':
    handler = RotatingFileHandler('yapki.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(host=host, port=port, debug=True)

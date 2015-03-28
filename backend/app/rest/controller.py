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
# (c) yafra.org, 2015, Switzerland
#
#-------------------------------------------------------------------------------
#
# show html index page
#
__author__ = 'mwn'

#import imp
#database = imp.load_source('database', 'database.py')
from ..database import Database

from flask import Blueprint, jsonify, make_response, json, current_app

restBp = Blueprint('rest', __name__)

@restBp.route('/db')
def DbPage():
    current_app.logger.info('start db list get')
    myDb = Database()
    #indexContent = myDb.certlist("/data/pki/yapki/index.txt")
    indexContent = myDb.certlist("/work/repos/git/yapki/backend/tests/index.txt")
    current_app.logger.debug(indexContent)
    json_data = json.dumps(indexContent)
    current_app.logger.debug(json_data)
    response = make_response(json.dumps(indexContent), 200)
    response.headers.add('Content-Type', 'application/json')
    return response


@restBp.route("/info")
def InfoPage():
    return jsonify(version='1.0.1',
                   status='OK')

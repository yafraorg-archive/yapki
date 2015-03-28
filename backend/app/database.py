#!/usr/bin/python
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
# python ssl/tls database module
#
# the structure of the index.txt openssl file is somehow defined here
# https://github.com/openssl/openssl/blob/master/apps/apps.h
# search for DB_type define
#
# http://www.ietf.org/rfc/rfc5280.txt (overall PKIX RFC)
# http://stackoverflow.com/questions/6464129/certificate-subject-x-509 (structure of subject string)
#
__author__ = 'mwn'
import re

class Database:
    def __init__(self):
        self.description = "YAPKI - openssl index database"
        self.author = "yafra.org - Martin Weber"
        print(self.author)

    def certlist(self, filename):
        certs = []
        with open(filename, 'r') as infile:
            for line in infile:
                certEntry = {}
                newline = line.rstrip('\n')
                certFields = newline.split('\t')
                certEntry['type'] = certFields[0]
                certEntry['expdate'] = certFields[1]
                certEntry['revdate'] = certFields[2]
                certEntry['serial'] = certFields[3]
                certEntry['file'] = certFields[4]
                certEntry['name'] = certFields[5]
                # CN=(.+?)/
                # emailAddress=(.+?)$ or \\n on the end
                cn = re.search("CN=(.+?)/", certEntry['name'])
                certEntry['cn'] = cn.group(1)
                cn = re.search("emailAddress=(.+?)$", certEntry['name'])
                certEntry['email'] = cn.group(1)
                certs.append(certEntry)
        return certs

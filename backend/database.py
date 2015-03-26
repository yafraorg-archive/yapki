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
__author__ = 'mwn'

#An example of a class
class Database:
    def __init__(self):
        self.description = "YAPKI - openssl index database"
        self.author = "yafra.org - Martin Weber"
        print(self.author)

    def certlist(self, filename):
        certs = []
        certEntry = {}
        with open(filename, 'r') as infile:
            for line in infile:
                certFields = line.split('\t')
                certEntry = {'type': certFields[0], 'expdate': certFields[1], 'revdate': certFields[2],
                             'serial': certFields[3], 'file': certFields[4], 'name': certFields[5]}
                certs.append(certEntry)
        return certs

# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
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
# python test unit
__author__ = 'mwn'

import imp
database = imp.load_source('database', 'app/database.py')

import sys
import unittest
from database import Database
import logging

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database()

    def testList(self):
        x = self.db.certlist('tests/index.txt')
        log= logging.getLogger( "yafratest" )
        log.debug( "this= %s", x )
        self.assertIsNotNone(x)

if __name__ == '__main__':
    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "yafratest" ).setLevel( logging.DEBUG )
    unittest.main()

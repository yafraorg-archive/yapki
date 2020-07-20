# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
#  Copyright 2020 yafra.org
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#-------------------------------------------------------------------------------
#
# YAPKI certificate file
import re
from utils.utils import decode_time
from datetime import date, datetime
from typing import List
from model.schemas import Certificate


def read(filename: str) -> List[Certificate]:
    certlist: List[Certificate] = []
    with open(filename, 'r') as infile:
        for line in infile:
            newline = line.rstrip('\n')
            certFields = newline.split('\t')
            # CN=(.+?)/
            # emailAddress=(.+?)$ or \\n on the end
            myCn = re.search("CN=(.+?)/", certFields[5])
            myEmail = re.search("emailAddress=(.+?)$", certFields[5])
            myExpDate = datetime.strptime(certFields[1], '%y%m%d%H%M%SZ')
            # certificate revokation date (only set if revoked)
            # decode_time(certFields[2], "%y%m%d%H%M%SZ")
            if certFields[2] and not certFields[2].isspace():
                myRevDate = datetime.strptime(certFields[2], '%y%m%d%H%M%SZ')
            else:
                # the string is empty
                myRevDate = 0
            certificate = Certificate(state=certFields[0], usage=1, expdate=myExpDate,
                                      revdate=myRevDate, serial=certFields[3],
                                      file=certFields[4], common_name=myCn.group(1),
                                      distinguished_name=certFields[5], owner_id=1, email=myEmail.group(1))
            certlist.append(certificate)
    return certlist
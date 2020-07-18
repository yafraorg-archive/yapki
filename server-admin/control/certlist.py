import re
from utils.utils import decode_time
from datetime import date, datetime
from typing import List
from model.certificate import Certificate


def certlist(filename: str) -> List[Certificate]:
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
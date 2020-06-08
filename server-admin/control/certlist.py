import re
from utils.utils import decode_time
from typing import List
from model.certificate import Certificate


def certlist(filename: str) -> List[Certificate]:
    certs = List[Certificate]
    certlist = certs()
    with open(filename, 'r') as infile:
        for line in infile:
            newline = line.rstrip('\n')
            certFields = newline.split('\t')
            if certFields[3] and not certFields[3].isspace():
                mySerial = certFields[3]
            else:
                # the string is empty
                mySerial = "empty"

            # certificate date's
            # decode_time(certFields[2], "%y%m%d%H%M%SZ")
            if certFields[2] and not certFields[2].isspace():
                myRevdate = certFields[2][:-1]
            else:
                # the string is empty
                myRevdate = "0"
            myExpdate = certFields[1][:-1]
            certificate = Certificate(id=1, type=certFields[0], expdate=int(myExpdate),
                                      revdate=int(myRevdate), serial=mySerial,
                                      file=certFields[4], common_name=certFields[4], valid=True,
                                      description="test", owner_id=1, email="test")
            # CN=(.+?)/
            # emailAddress=(.+?)$ or \\n on the end
            #cn = re.search("CN=(.+?)/", certFields[4])
            #certificate.common_name = cn.group(1)
            #cn = re.search("emailAddress=(.+?)$", certFields[4])
            #certificate.email = cn.group(1)
            certlist.append(certificate)
    return certlist
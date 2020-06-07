import re
from utils.utils import decode_time
from typing import List
from model.certificate import Certificate


def certlist(filename: str) -> List[Certificate]:
    certs = List[Certificate]
    with open(filename, 'r') as infile:
        for line in infile:
            certEntry = {}
            newline = line.rstrip('\n')
            certFields = newline.split('\t')
            # decode_time(certFields[2], "%y%m%d%H%M%SZ")
            myRevdate = certFields[2][:-1]
            myExpdate = certFields[1][:-1]
            certificate = Certificate(id=1, type=certFields[0], expdate=int(myExpdate),
                                      revdate=int(myRevdate), serial=int(certFields[3]),
                                      file=certFields[4], name=certFields[4], common_name="test", valid=True,
                                      description="test", owner_id=1)
            # CN=(.+?)/
            # emailAddress=(.+?)$ or \\n on the end
            cn = re.search("CN=(.+?)/", certificate.name)
            certificate.common_name = cn.group(1)
            cn = re.search("emailAddress=(.+?)$", certificate.name)
            certificate.email = cn.group(1)
            certs.append(certificate)
    return certs
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
            certEntry['type'] = certFields[0]
            certEntry['expdate'] = decode_time(certFields[1], "%y%m%d%H%M%SZ")
            certEntry['revdate'] = decode_time(certFields[2], "%y%m%d%H%M%SZ")
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
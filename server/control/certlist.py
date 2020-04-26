def certlist(self, filename):
    certs = []
    with open(filename, 'r') as infile:
        for line in infile:
            certEntry = {}
            newline = line.rstrip('\n')
            certFields = newline.split('\t')
            certEntry['type'] = certFields[0]
            certEntry['expdate'] = self.decode_time(certFields[1], "%y%m%d%H%M%SZ")
            certEntry['revdate'] = self.decode_time(certFields[2], "%y%m%d%H%M%SZ")
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


def decode_time(self, obj, format):
    try:
        parsedDate = dt.datetime.strptime(obj, format)
        return parsedDate.strftime("%Y-%m-%dT%H:%M:%S")
    except:
        return 0

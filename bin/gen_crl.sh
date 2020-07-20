#!/bin/sh
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
#
# function:	generate revocation list
#-------------------------------------------------------------------------------

# arguments are: 1: crl days
if [ -z "$1" ]; then
        echo Please specify crl days
        exit
fi

openssl ca -gencrl -config openssl.cnf -crldays $1 -crlexts crl_ext -out nissle/crl/canissle.crl
openssl crl -in nissle/crl/canissle.crl -outform DER -out nissle/crl/canissle-der.crl

# copy crl to apache2
cp nissle/crl/canissle.crl /opt/etc/apache2/ssl
/usr/local/apache/bin/apachectl restart

cp nissle/crl/*.crl /share/Nissle/mwn/.


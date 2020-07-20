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
# function:	PKI generate web certificate (apache mod_ssl)
#
# argument: cert basename
#
# CVS tag:   $Name:  $
# author:    $Author: mwn $
# revision:  $Revision: 16 $
#-------------------------------------------------------------------------------

# arguments are: 1: certificate basename
if [ -z "$1" ]; then
        echo "Please specify a basename to be used for the new certificate"
        exit
fi

# create WWW server request
openssl genrsa -des3 -out $1.key 1024
openssl req -config openssl.cnf -new -sha1 -key $1.key -out $1.csr

# sign WWW server request with CA
echo "\nSign the new certificate now through a CA"
openssl ca -config openssl.cnf -policy policy_anything -out $1.crt -infiles $1.csr

# create RSA private key with password for automatic server startup
echo "\nCreate a new RSA private key which does not need a password to enable automatic server startup"
cp $1.key $1.key.org
openssl rsa -in $1.key.org -out $1.key

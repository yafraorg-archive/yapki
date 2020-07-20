#!/usr/bin/env bash
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
# generate a CA structure and the root CA certificate
#
printf "Start to generate a new CA configuration\n\n"
# directory structure:
# root directory is yapki/
CATOP="yapki"

SSLEAY_CONFIG="-config ./openssl.cnf"
DAYS="-days 1095"    # 3 year
CADAYS="-days 7300"   # 10 years
REQ="openssl req $SSLEAY_CONFIG"
CA="openssl ca $SSLEAY_CONFIG"
VERIFY="openssl verify"
X509="openssl x509"
PKCS12="openssl pkcs12"

CAKEY="cakey.pem"
CAREQ="careq.pem"
CACERT="cacert.pem"

function initialize_ca_directory {
    echo "Creating a new CA root directory structure now"
    mkdir $CATOP
    mkdir $CATOP/certs
    mkdir $CATOP/crl
    mkdir $CATOP/newcerts
    mkdir $CATOP/private

    # generate a random file
    base64 /dev/urandom | head -c 10000 > $CATOP/private/random.txt

    # create empty openssl database file
    touch $CATOP/index.txt

    # create crlnumber file
    echo "01\n" > $CATOP/crlnumber
}



if [ -d "$CATOP" ]; then
  read -p 'A CA directory already exists, do you want to delete and initialize it? (yes/no): ' caDelete
  if [[ "$caDelete" == "yes" ]]; then
    mv $CATOP delete_$RANDOM
    mkdir $CATOP
    printf "CA directory deleted (in fact moved as delete_)"
    initialize_ca_directory
  else
    printf "Creation process will exit now. Nothing to initialize"
    exit
  fi
else
    mkdir $CATOP
    printf "Create a new CA directory and start to create CA certificate"
    initialize_ca_directory
fi

printf "Making CA certificate ...\n"
$REQ -new -keyout ${CATOP}/private/$CAKEY -out ${CATOP}/$CAREQ
$CA -create_serial -out ${CATOP}/$CACERT $CADAYS -batch -keyfile ${CATOP}/private/$CAKEY -selfsign -extensions v3_ca -infiles ${CATOP}/$CAREQ

printf "DONE!"
exit

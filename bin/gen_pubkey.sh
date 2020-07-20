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
# function:	generate public key from private key
#-------------------------------------------------------------------------------

# arguments are: 1: crl days
if [ -z "$1" ]; then
        echo Please specify private key as PEM file
        exit
fi

echo "creating the public key out of your private key $1 as file public_key.pem"
openssl rsa -in $1 -pubout -out public_key.pem


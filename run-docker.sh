#!/usr/bin/env bash
#-------------------------------------------------------------------------------
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# (c) yafra.org, 2002, Switzerland
#
#-------------------------------------------------------------------------------
#
# docker run script
#
export BASENODE=/work/repos
export YAPKI=$BASENODE/yapki
export YAFRA=$BASENODE/yafra
export YAFRADB=$BASENODE/yafra-database

export PKISERVER=/work/pkiserver
test -d $PKISERVER || mkdir -p $PKISERVER

echo "update all relevant yafra git repos now"
cd $YAPKI
git pull

echo "install python server and update requirements now"
cp $YAPKI/backend/* $PKISERVER
cp -r $YAPKI/backend/app $PKISERVER
cd $PKISERVER
#pip install -r requirements.txt
pip3 install -r requirements.txt

# TODO update requirements and nodejs packages

#echo "start yapki by run-yapki.sh script"
#./run-yapki.sh

echo "done - run-docker"

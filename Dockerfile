#
#  Copyright 2015 yafra.org
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
# yafra.org PKI docker image
# https://github.com/yafraorg/yafra/wiki/Yapki
#

# source is yafra ubuntu
FROM alpine:3
MAINTAINER Martin Weber <info@yafra.org>

# Install common packages
RUN \
  apk update && \
  apk upgrade && \
  apk add --update git openssl openssl-dev nodejs supervisor apache2 apache2-mod-wsgi apache2-ssl libffi libffi-dev build-base gcc && \
#  apk add --update python python-dev py-pip py-cffi
  apk add --update python3 python3-dev

# Install git repositories
RUN \
  mkdir -p /work && \
  cd /work

WORKDIR /work
COPY . /work

RUN cd /work/server-admin && \
  python3 -m ensurepip && \
  rm  -r /usr/lib/python*/ensurepip && \
  pip3 install --upgrade pip setuptools && \
  pip3 install -r requirements.txt

# Expose ports
EXPOSE 8081
EXPOSE 8082

ENTRYPOINT ["/work/repos/yapki/run-docker.sh"]

#CMD ["busybox /bin/bash"]

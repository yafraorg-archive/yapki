#
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
# yafra.org NodeJS / MEAN.io docker image
#

# source is alpine
FROM node:lts_alpine
MAINTAINER Yafra <yafraorg@gmail.com>

# Install global npm packages and phantomjs-prebuilt
RUN cd /work && \
  npm install -g gulp-cli bower phantomjs-prebuilt

RUN cd /work/repos/yafra-nodejs/restserver && \
  npm install

VOLUME ["/data"]

EXPOSE 3000

ENTRYPOINT ["/work/repos/yafra-nodejs/run-docker.sh"]


# Default command
#CMD ["/bin/bash"]


#CMD ["/work/run-docker.sh"]
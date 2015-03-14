#!/bin/sh
#
# LOCAL BUILD
# used for CI services like Jenkins, Shippable, Travis-CI
#
# variables must be set by CI service
# setup local environment first https://github.com/yafraorg/yafra/wiki/Development-Environment
export BASENODE=/work/repos/yapki
export WORKNODE=/work/yafra-runtime
#export SYSADM=/work/repos/git/yafra/org.yafra.sysadm
#export YAFRATOOLS=$SYSADM/defaults
#export YAFRABIN=$SYSADM/defaults/scripts
export YAFRADOC=$WORKNODE/doc
export YAFRAMAN=$WORKNODE/man
export YAFRAEXE=$WORKNODE/bin
    
export PATH=$PATH:$YAFRABIN:$YAFRAEXE

echo "YAPKI local build starting"
echo "environment is WORKNODE = $WORKNODE - BASENODE = $BASENODE"
test -d $WORKNODE/apps || mkdir -p $WORKNODE/apps
test -d $WORKNODE/bin || mkdir -p $WORKNODE/bin

# set database server here
export DBSERVER=$DB_PORT_3306_TCP_ADDR
#export DBSERVER=192.168.9.10

cd backend
pip install -r requirements.txt --use-mirrors
cd ../www
npm install
bower install
# npm run update-webdriver
# node_modules/.bin/webdriver-manager update
# sleep 1 # give server time to start
cd ..
mkdir -p shippable/testresults
mkdir -p shippable/codecoverage
mkdir -p shippable/screenshots
#export DISPLAY=:99.0
#sh -e /etc/init.d/xvfb start
www/node_modules/.bin/http-server -p 8081 www/app/ &
sleep 1

#  - node_modules/.bin/karma start karma.conf.js --no-auto-watch --single-run --reporters=dots --browsers=Firefox
#  - node_modules/.bin/protractor e2e-tests/protractor.conf.js --browser=firefox
cd www
node_modules/.bin/gulp karma
node_modules/.bin/gulp protractor
node_modules/.bin/gulp jshint
node_modules/.bin/gulp changelog
node_modules/.bin/istanbul report cobertura --dir ../shippable/codecoverage/

cd ../backend
export PYTHONPATH=$PYTHONPATH:.
#coverage run -m unittest test/TestDatabase.py
nosetests test/TestDatabase.py --with-xunit --xunit-file=../shippable/testresults/nosetests.xml
coverage xml -o ../shippable/codecoverage/coverage.xml
cd ..

#
# start yafra test first as this creates the tables if they are still missing
echo "============================================================"
echo " TEST CASE 1: curl the entry page"
echo "============================================================"
#curl localhost

echo "done - save in /work"

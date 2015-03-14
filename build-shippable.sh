#!/bin/sh
#
# used for CI services like Jenkins, Shippable, Travis-CI
#
# variables must be set by CI service
# setup local environment first https://github.com/yafraorg/yafra/wiki/Development-Environment
export BASENODE=/home/shippable/workspace/src/github.com/yafraorg/yapki
export WORKNODE=/work/yafra-runtime
export SYSADM=/work/repos/yafra/org.yafra.sysadm
export YAFRATOOLS=$SYSADM/defaults
export YAFRABIN=$SYSADM/defaults/scripts
export YAFRADOC=$WORKNODE/doc
export YAFRAMAN=$WORKNODE/man
export YAFRAEXE=$WORKNODE/bin
    
export PATH=$PATH:$YAFRABIN:$YAFRAEXE

echo "YAPKI build starting"
echo "environment is WORKNODE = $WORKNODE - BASENODE = $BASENODE"
test -d $WORKNODE/apps || mkdir -p $WORKNODE/apps
test -d $WORKNODE/bin || mkdir -p $WORKNODE/bin



echo "done - save in /work"

#!/bin/bash
# 

SCRIPT_DIR="$( cd "$( dirname "$0" )" >/dev/null 2>&1 && pwd )"

source $SCRIPT_DIR/CONFIG
source $SCRIPT_DIR/utils.sh

parseCommandLine

rm -rf $SCRIPT_DIR/tmp

docker-compose -f $SCRIPT_DIR/docker-compose.yml down -v

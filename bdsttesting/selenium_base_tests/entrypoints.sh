#!/bin/bash
set -e
echo "***** SeleniumBase Docker Machine *****"
echo "Checking for ZAP"
./wait-for-it.sh 172.28.1.1:8090 -t 60
echo "Checking for WebGoat"
./wait-for-it.sh 172.28.1.2:8080 -t 60

# we actually have to run two selenium tests first one to register a user

exec "$@"
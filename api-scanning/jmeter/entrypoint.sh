#!/usr/bin/env bash
# Inspired from https://github.com/hhcordero/docker-jmeter-client
# and https://github.com/justb4/docker-jmeter
# Basically runs jmeter, assuming the PATH is set to point to JMeter bin-dir (see Dockerfile)
#
# This script expects the standdard JMeter command parameters.
#
set -e
freeMem=`awk '/MemFree/ { print int($2/1024) }' /proc/meminfo`
s=$(($freeMem/10*8))
x=$(($freeMem/10*8))
n=$(($freeMem/10*2))
export JVM_ARGS="-Xmn${n}m -Xms${s}m -Xmx${x}m"

rm -rf /jmeter/results/jmeter/security > /dev/null 2>&1


echo "START Running Jmeter on `date`"
echo "JVM_ARGS=${JVM_ARGS}"
echo "jmeter args=$@"

./wait-for-it.sh zap:8090 -t 60
# Keep entrypoint simple: we must pass the standard JMeter arguments
jmeter $@
echo "END Running Jmeter on `date`"

mkdir -p /jmeter/results/zap/html
mkdir -p /jmeter/results/zap/json

sleep 10

curl -X GET http://zap:8090/HTML/core/view/alerts > /jmeter/results/zap/html/LoginTesting.HTML
curl -X GET http://zap:8090/JSON/core/view/alerts > /jmeter/results/zap/json/LoginTesting.JSON
curl -X GET http://zap:8090/JSON/core/action/shutdown/

python3 should_it_fail.py

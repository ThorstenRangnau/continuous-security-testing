#!/usr/bin/env bash
#
# Test the JMeter Docker image using a trivial test plan.

# Example for using User Defined Variables with JMeter
# These will be substituted in JMX test script
# See also: http://stackoverflow.com/questions/14317715/jmeter-changing-user-defined-variables-from-command-line
export TARGET_HOST="demo.testfire.net"
export TARGET_PORT="80"
export TARGET_PATH="/bank/login.aspx"
export TARGET_KEYWORD="Login"
export PROXY_HOST="192.168.178.10"
export PROXY_PORT="8090"

T_DIR=tests/security

# Reporting dir: start fresh
R_DIR=${T_DIR}/securityreport
rm -rf ${R_DIR} > /dev/null 2>&1
mkdir -p ${R_DIR}

/bin/rm -f ${T_DIR}/HTTP_Request.jtl ${T_DIR}/jmeter.log  > /dev/null 2>&1

./run.sh -Dlog_level.jmeter=DEBUG \
	-JTARGET_HOST=${TARGET_HOST} -JTARGET_PORT=${TARGET_PORT} \
	-JTARGET_PATH=${TARGET_PATH} \
	-H ${PROXY_HOST} -P ${PROXY_PORT} -N localhost \
	-n -t ${T_DIR}/HTTP_Request.jmx -l ${T_DIR}/HTTP_Request.jtl -j ${T_DIR}/jmeter.log \
	-e -o ${R_DIR}

	#-JTARGET_PATH=${TARGET_PATH} -JTARGET_KEYWORD=${TARGET_KEYWORD} \

echo "==== jmeter.log ===="
cat ${T_DIR}/jmeter.log

echo "==== Raw Test Report ===="
cat ${T_DIR}/HTTP_Request.jtl

echo "==== HTML Test Report ===="
echo "See HTML test report in ${R_DIR}/index.html"
# This dockerfile builds the zap stable release
FROM ubuntu:18.04
LABEL maintainer="psiinon@gmail.com"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -q -y --fix-missing \
	make \
	automake \
	autoconf \
	gcc g++ \
	openjdk-8-jdk \
	wget \
	curl \
	xmlstarlet \
	unzip \
	git \
	openbox \
	xterm \
	net-tools \
	python-pip \
	python3-pip \
	firefox \
	xvfb \
	x11vnc && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip zapcli python-owasp-zap-v2.4
RUN pip3 install --upgrade pip zapcli python-owasp-zap-v2.4

RUN useradd -d /home/zap -m -s /bin/bash zap
RUN echo zap:zap | chpasswd
RUN mkdir /zap && chown zap:zap /zap

WORKDIR /zap

#Change to the zap user so things get done as the right person (apart from copy)
USER zap

RUN mkdir /home/zap/.vnc

# Download and expand the latest stable release
RUN curl -s https://raw.githubusercontent.com/zaproxy/zap-admin/master/ZapVersions.xml | xmlstarlet sel -t -v //url |grep -i Linux | wget -nv --content-disposition -i - -O - | tar zxv && \
	cp -R ZAP*/* . &&  \
	rm -R ZAP* && \
	# Setup Webswing
	curl -s -L https://bitbucket.org/meszarv/webswing/downloads/webswing-2.5.10.zip > webswing.zip && \
	unzip webswing.zip && \
	rm webswing.zip && \
	mv webswing-* webswing && \
	# Remove Webswing demos
	rm -R webswing/demo/ && \
	# Accept ZAP license
	touch AcceptedLicense


ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
ENV PATH $JAVA_HOME/bin:/zap/:$PATH
ENV ZAP_PATH /zap/zap.sh

# Default port for use with zapcli
ENV ZAP_PORT 8080
ENV HOME /home/zap/

COPY . /zap/
COPY ./webswing.config /zap/webswing/
COPY ./policies /home/zap/.ZAP/policies/
# The scan script loads the scripts from dev home dir.
COPY ./scripts /home/zap/.ZAP_D/scripts/
COPY ./.xinitrc /home/zap/

#Copy doesn't respect USER directives so we need to chown and to do that we need to be root
USER root

RUN chown zap:zap /zap/* && \
	chown zap:zap /zap/webswing/webswing.config && \
	chown zap:zap -R /home/zap/.ZAP/ && \
	chown zap:zap /home/zap/.xinitrc && \
	chmod a+x /home/zap/.xinitrc

#Change back to zap at the end
USER zap

HEALTHCHECK --retries=5 --interval=5s CMD zap-cli status
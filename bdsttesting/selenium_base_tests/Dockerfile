FROM docker/compose

WORKDIR /usr/src/app

RUN apk update && apk add python3-dev curl
RUN pip3 install python-owasp-zap-v2.4

RUN apk update \
  && apk add python3-dev \
  && apk add curl \
  && apk add chromium chromium-chromedriver \
  && apk add build-base libffi-dev openssl-dev \
  && rm -rf /var/cache/apk/*

RUN pip3 install seleniumbase
RUN pip3 install pytest

RUN seleniumbase install chromedriver

COPY tests/* user/src/app/

COPY wait-for-it.sh /usr/src/app
RUN chmod +x /usr/src/app/wait-for-it.sh

RUN mkdir -p /results

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
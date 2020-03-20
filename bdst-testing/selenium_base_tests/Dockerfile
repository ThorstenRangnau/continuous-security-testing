FROM python:3.6

WORKDIR /usr/src/app

RUN apt-get update \
  && apt-get install -y chromium-driver \
  && apt-get clean

RUN pip install seleniumbase

RUN seleniumbase install chromedriver

COPY test_register_web_goat_SB.py /usr/src/app
COPY entrypoints.sh /
COPY wait-for-it.sh /usr/src/app

RUN chmod +x /usr/src/app/wait-for-it.sh

ENTRYPOINT ["/entrypoints.sh"]
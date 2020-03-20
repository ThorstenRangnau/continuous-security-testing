FROM python:3.6

RUN pip install seleniumbase

RUN seleniumbase install chromedriver

COPY ./userregistration_SB.py .

CMD pytest userregistration_SB.py --proxy=http://zap:8090 --headless --browser=chrome
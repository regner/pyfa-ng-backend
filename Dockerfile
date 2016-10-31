

FROM debian:latest

ADD . /app/

WORKDIR /app/

RUN apt-get update -qq \
&& apt-get upgrade -y -qq \
&& apt-get install -y -qq python-dev python-pip \
&& apt-get autoremove -y \
&& apt-get clean autoclean \
&& pip install -qU pip \
&& pip install -r requirements.txt

EXPOSE 8000

CMD gunicorn wsgi:app -w 1 -b 0.0.0.0:8000 --log-level info --timeout 120 --pid /app/pyfa_ng_backend.pid
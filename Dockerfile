FROM debian:jessie
RUN apt-get update && apt-get install -y python-pip
WORKDIR /opt/marina/web
ADD requirements.txt /opt/conduit/requirements.txt
RUN pip install pip --upgrade
RUN pip install -r requirements.txt

ADD . /opt/marina/web


CMD /usr/bin/python -u marina-web.py

EXPOSE 5000

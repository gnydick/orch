FROM python:3.7.0

ENV FLASK_APP=app.py
ENV FLASK_CFG=config/prod.cfg
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get -y install python3 && \
    apt-get -y install python3-pip && \
    apt-get -y clean

RUN mkdir /orch
WORKDIR /orch

ADD /requirements.txt /orch/requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

ADD /controllers /orch/controllers
ADD /converters /orch/converters
ADD /models /orch/models
ADD /templates /orch/templates
ADD /views /orch/views
ADD /ajax_loader /orch/ajax_loader
ADD /app.py /orch/
ADD /base.py /orch/
ADD /db.py /orch/


RUN chown -R nobody:nogroup /orch
USER nobody

CMD gunicorn app:app -b 0.0.0.0:5000 --keep-alive 86400 --preload --workers=16 -k gevent

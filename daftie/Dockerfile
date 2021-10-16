FROM python:3.8

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

WORKDIR /daftie

COPY ./daftie ./daftie
COPY ./scrapy.cfg ./scrapy.cfg
COPY ./docker-entrypoint.sh ./docker-entrypoint.sh

RUN useradd -c 'daft.ie crawler user' -d /data -m -s /bin/false -U  daftie

RUN chown -R daftie:daftie .

USER daftie

VOLUME /data

ENTRYPOINT "/daftie/docker-entrypoint.sh"

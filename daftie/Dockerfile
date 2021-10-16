FROM python:3.8

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

WORKDIR /daftie

COPY ./daftie ./daftie
COPY ./scrapy.cfg ./scrapy.cfg

RUN useradd -c 'daft.ie crawler user' -d /data -m -s /bin/false -U  daftie

RUN chown -R daftie:daftie .

USER daftie

VOLUME /data

CMD ["scrapy", "crawl", "rent", "-O", "/data/daftie-$(date +%F-%H-%M).csv", "-t", "csv"]

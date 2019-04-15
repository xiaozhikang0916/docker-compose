FROM python:3.6-alpine
LABEL MAINTAINER="trim21<trim21me@gmail.com>"

EXPOSE 8888

ENV LANG C.UTF-8
ENV TRAVIS_CI 1
ENV BGMI_PATH=/bgmi

ENV PIP_ARGS='--no-cache-dir  -i https://mirrors.ustc.edu.cn/pypi/web/simple'

COPY ./bgmi/requirements.txt /requirements.txt

RUN pip install $PIP_ARGS https://github.com/BGmi/bgmi/tarball/f2d76a71b39ab1810915ad73b3ad849b3ce2306f

COPY ./entrypoint.sh /entrypoint.sh

ENTRYPOINT  ["sh", "/entrypoint.sh"]

CMD ["start_server"]


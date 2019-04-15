FROM alpine:edge
LABEL MAINTAINER=trim21<trim21me@gmail.com>

EXPOSE 6800

ENV PACKAGE "aria2"

# Install package using --no-cache to update index and remove unwanted files
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories && \
    apk add --upgrade --no-cache $PACKAGE


COPY ./entrypoint.sh /entrypoint.sh

CMD sh /entrypoint.sh

FROM alpine:latest

RUN apk add --no-cache bash procps coreutils

WORKDIR /app

COPY scripts/monitor.sh /app/monitor.sh

RUN chmod +x /app/monitor.sh

ENV INTERVAL=5

CMD ["/app/monitor.sh"]
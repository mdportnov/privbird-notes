FROM alpine:latest

ADD ./entry_point.sh /

RUN apk update \
	&& apk upgrade
RUN apk add socat
RUN apk add --update-cache \
			--repository http://dl-cdn.alpinelinux.org/alpine/edge/testing/ \
			--allow-untrusted --update tor

RUN chmod +x /entry_point.sh

ADD ./torrc /etc/tor/torrc


EXPOSE 5000

ENTRYPOINT ["/entry_point.sh"]
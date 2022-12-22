FROM nginx:1.21

RUN apt update && apt install -y iptables
RUN rm /etc/nginx/conf.d/default.conf
RUN unlink /var/log/nginx/access.log
RUN unlink /var/log/nginx/error.log

COPY nginx.conf /etc/nginx/conf.d

COPY entrypoint.sh /app/entrypoint.sh

ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]

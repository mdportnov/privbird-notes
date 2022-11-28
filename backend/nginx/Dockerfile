FROM nginx:1.21

RUN apt update && apt install -y fail2ban iptables
RUN rm /etc/nginx/conf.d/default.conf
RUN unlink /var/log/nginx/access.log
RUN unlink /var/log/nginx/error.log

COPY nginx.conf /etc/nginx/conf.d

COPY ./fail2ban/jail.conf /etc/fail2ban/jail.local
COPY ./fail2ban/nginx-req-limit.conf /etc/fail2ban/filter.d/nginx-req-limit.conf

COPY entrypoint.sh /app/entrypoint.sh

ENTRYPOINT ["/bin/sh", "/app/entrypoint.sh"]

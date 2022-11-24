FROM nginx:1.21

RUN apt update && apt install -y fail2ban
RUN rm /etc/nginx/conf.d/default.conf

COPY jail.conf /etc/fail2ban/jail.local
COPY nginx.conf /etc/nginx/conf.d
COPY entrypoint.sh /app/entrypoint.sh

ENTRYPOINT ["/bin/sh", "/app/entrypoint.sh"]

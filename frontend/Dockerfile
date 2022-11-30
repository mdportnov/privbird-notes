FROM node:19-alpine as builder

ARG mode

WORKDIR /app/

COPY . .

RUN npm install && \
    npm run build::${mode}

FROM nginx:1.21

RUN apt update && apt install -y fail2ban iptables

RUN rm /etc/nginx/conf.d/default.conf

RUN unlink /var/log/nginx/access.log && \
    unlink /var/log/nginx/error.log

COPY --from=builder /app/dist/ /app/dist/

COPY ./nginx/fail2ban/jail.conf /etc/fail2ban/jail.local

COPY ./nginx/fail2ban/nginx-req-limit.conf /etc/fail2ban/filter.d/nginx-req-limit.conf

COPY ./nginx/nginx.conf /etc/nginx/conf.d

COPY ./nginx/entrypoint.sh /app/entrypoint.sh

ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]

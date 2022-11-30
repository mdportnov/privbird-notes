#!/bin/bash

echo "Start fail2ban service"
fail2ban-client start

echo "Enable error.log output"
tail -f /var/log/nginx/error.log > /dev/stderr &

echo "Enable fail2ban.log output"
tail -f /var/log/fail2ban.log > /dev/stdout &

echo "Substitute environment variables"
envsubst < /tmp/nginx.template.conf > /etc/nginx/conf.d/nginx.conf

echo "Start nginx daemon"
nginx -g "daemon off;"

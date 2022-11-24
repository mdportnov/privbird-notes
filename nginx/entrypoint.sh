#!/bin/bash

echo "Start fail2ban service"
fail2ban-client start

echo "Start nginx daemon"
nginx -g "daemon off;"

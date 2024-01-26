#!/bin/bash
# Bash script thatsends a request to a URL passed as an arg, display only status code
curl -s -o /dev/null -w "%{http_code}" "$1"

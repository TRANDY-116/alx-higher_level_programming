#!/bin/bash
# Bash scrip that takes in a URL as arg, sends a GET request and display body
curl -s -H "X-School-User-Id: 98" "$1"

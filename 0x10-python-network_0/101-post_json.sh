#!/bin/bash
# Bash script that sends a JSON POST request to a URL passed as first arg and display the body
curl -s -H "COntent-Type: application/json" -X POST "$1" -d "$(cat "$2")"

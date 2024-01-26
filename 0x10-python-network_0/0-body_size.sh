#!/bin/bash
# Bash script that takes ina URL, sends a request to that Url and Displays the size of the body of the response
curl -s "$1" | wc -c

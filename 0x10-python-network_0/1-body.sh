#!/bin/bash
# Scriot that takes in a Url and sends a GET request to the URL and displays the body fo the response
curl -sL -X GET "$1"

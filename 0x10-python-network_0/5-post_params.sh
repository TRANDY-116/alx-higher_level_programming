#!/bin/bash
# Bash script that takes in a URL and sends a POST request, and adds the body
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"

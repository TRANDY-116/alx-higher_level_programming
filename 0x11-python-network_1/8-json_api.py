#!/usr/bin/python3
""" Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter."""

import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    payload = {"q": q}

    url = "http://0.0.0.0:5000/search_user"

    req = requests.post(url, data=payload)

    try:
        response = req.json()
        if not response:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")

#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and
displays the body of the response."""

import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    req = requests.get(url)

    if req.stats_code >= 400:
        the_page = ("Error code: {}".format(req.status_code))
        print(the_page)
    else:
        print(req.text)

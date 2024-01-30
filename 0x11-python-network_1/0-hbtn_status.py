#!/usr/bin/python3
""" python script that fetches https://alx-intranet.hbtn.io/status """

import urllib.request
""" Importing the urrlib package """


if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')

    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        utf8 = the_page.decode("utf-8")

        print("Body response:")
        print("\t- type: {}".format(type(the_page)))
        print("\t- content: {}".format(the_page))
        print("\t- utf8 content: {}".format(utf8))

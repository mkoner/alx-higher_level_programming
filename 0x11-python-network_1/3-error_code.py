#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8)
"""

if __name__ == "__main__":
    import sys
    import urllib.parse as parser
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError, URLError
    req = Request(sys.argv[1])
    try:
        response = urlopen(req)
    except HTTPError as e:
        print("Error code: {}".format(e.code))
    except URLError as e:
        print("Cannot establish connexion")

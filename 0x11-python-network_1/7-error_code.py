#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the body of the response
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    res = requests.get(argv[1])
    if res.status_code < 400:
        print(res.text)
    else:
        print("Error code: {}".format(res.status_code))

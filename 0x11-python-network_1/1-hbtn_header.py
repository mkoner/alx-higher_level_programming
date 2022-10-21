#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response
"""

if __name__ == "__main__":
    import sys
    import urllib.request as my_request
    with my_request.urlopen(sys.argv[1]) as my_response:
        print(my_response.headers.get('X-Request-Id'))

#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the 
response (decoded in utf-8)
"""

if __name__ == "__main__":
    import urllib.parse as parser
    import urllib.request as my_request
    from sys import argv
    values = {'email': argv[2]}
    data = parser.urlencode(values).encode('utf-8')
    req = my_request.Request(argv[1], data)
    with my_request.urlopen(req) as res:
        print("Your email is: {}".format(res.read().decode('utf-8')))

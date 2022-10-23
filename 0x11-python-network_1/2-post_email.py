"""
Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)
"""

if __name__ == "__main__":
    import urllib.parse as parser
    import urllib.request as my_requesit
    import sys
    values = {'email': sys.argv[2]}
    data = parser.urlencode(values).encode('utf-8')
    req = my_request.Request(sys.argv[1], data)
    with my_request.urlopen(req) as my_resonse:
        print('{}'.format(my_resonse.read().decode('utf-8')))

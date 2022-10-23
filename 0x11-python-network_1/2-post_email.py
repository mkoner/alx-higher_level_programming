#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter
"""

if __name__ == "__main__":
    import sys
    import urllib.request as my_request
    import urllib.parse as my_parser
    my_url = sys.argv[1]
    my_email = sys.argv[2]
    my_value = {'email': my_email}
    my_req = my_request.Request(my_url, my_data)
    with my_request.urlopen(my_req) as my_response:
        page = my_response.read()
        print("Your email is: {}".format(page.decode('utf-8')))

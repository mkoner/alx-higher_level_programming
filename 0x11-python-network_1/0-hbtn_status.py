#!/usr/bin/python3
"""
Script to fetch from https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import urllib.request as my_request
    with my_request.urlopen('https://alx-intranet.hbtn.io/status') as my_response:
        my_page = my_response.read()
        print('Body response:')
        print("\t- type: {}".format(type(my_page)))
        print("\t- content: {}".format(my_page))
        print("\t- utf8 content: {}".format(my_page.decode('utf-8')))

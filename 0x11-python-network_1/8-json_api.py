#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    q = argv[1] if len(argv) > 1 else ""
    res = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        json_response = res.json()
        id = json_response.get('id')
        name = json_response.get('name')
        if len(json_response) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(id, name))
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")

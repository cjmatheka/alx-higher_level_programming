#!/usr/bin/python3
"""A script that:
Displays the X-Request-Id header variable
"""

if __name__ == "__main__":

    import sys
    import requests

    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))

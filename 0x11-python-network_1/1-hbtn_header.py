#!/usr/bin/python3

"""A Script that does the following:
 - Takes a url as argument
 - Sends a request to the url
 - Displays the value of the X-Request-Id variable.
"""

if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        headers = dict(response.getheaders())
        print(headers.get("X-Request-Id"))

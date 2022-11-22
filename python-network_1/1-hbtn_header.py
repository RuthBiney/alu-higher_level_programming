#!/usr/bin/python3
"""Fetches header"""


import urllib.request
import sys


if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as reply:
        header = reply.info()
        print(header['X-Request-Id'])


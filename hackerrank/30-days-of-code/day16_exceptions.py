#!/bin/python3

import sys


S = input().strip()


try:
    r = int(S)
    print(r)
except (ValueError):
    print("Bad String")

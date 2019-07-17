#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())

r = "Weird"

if N % 2 == 0:
    if 2 <= N <= 5:
        r = "Not Weird"
    elif 6 <= N <= 20:
        r = "Weird"
    else:
        r = "Not Weird"

print(r)

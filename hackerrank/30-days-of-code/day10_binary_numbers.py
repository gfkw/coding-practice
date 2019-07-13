#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    bin = "{0:b}".format(n)
    ones_list = list(filter(None, str(bin).split("0")))
    print(len(max(ones_list)))

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)

if __name__ == '__main__':

    n = int(input())
    print(factorial(n))

"""
explain plan:

    factorial(5) = 120 <─────────┐9º
  1º└─> 5 * factorial(4) = 5 * 24 <─────┐8º
          2º└─> 4 * factorial(3) = 4 * 6 <──────┐7º
                  3º└─> 3 * factorial(2) = 3 * 2 <──────┐6º
                          4º└─> 2 * factorial(1) = 2 * 1 <─┐
                                  5º└─> 1 ─────────────────┘

"""

import numpy as np

def get_middle(s):
    size = len(s)
    mid = int(np.median(np.arange(len(s))))
    mid1 = int(round(mid))
    mid2 = int(round(mid)) + 2

    if size % 2 != 0:
        return s[mid]
    else:
        return s[mid1:mid2]

"""
best solution:

def get_middle(s):
   return s[(len(s)-1)/2:len(s)/2+1]
"""

"""
Given an array, a, of size n distinct elements, sort the array in ascending order using the Bubble Sort algorithm above.
Once sorted, print the following 3 lines:

1. Array is sorted in numSwaps swaps.
where numSwaps is the number of swaps that took place.

2. First Element: firstElement
where firstElement is the first element in the sorted array.

3. Last Element: lastElement
where lastElement is the last element in the sorted array.

Hint: To complete this challenge, you will need to add a variable that keeps a running tally of all swaps that occur during execution.
"""

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

s = 0
c = True
while c:
    c = False
    for i in range(len(a)-1):
        #print("Before: ", a[i], a[i+1], a)
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            #print("After: ", a[i], a[i+1], a)
            s += 1
            c = True

#print(a)
print("Array is sorted in {} swaps.\nFirst Element: {}\nLast Element: {}".format(s,a[0],a[-1]))

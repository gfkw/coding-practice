"""
Create a function that returns an array containing the first l digits from the nth diagonal of Pascal's triangle.

n = 0 should generate the first diagonal of the triangle (the 'ones'). The first number in each diagonal should be 1.

If l = 0, return an empty array. Assume that both n and l will be non-negative integers in all test cases.

The Pascal's triangle Definition by Wiki:

The rows of Pascal's triangle are conventionally enumerated starting with row n = 0 at the top (the 0th row).
The entries in each row are numbered from the left beginning with k = 0 and are usually staggered relative to the numbers in the adjacent rows.
The triangle may be constructed in the following manner: In row 0 (the topmost row), there is a unique nonzero entry 1.
Each entry of each subsequent row is constructed by adding the number above and to the left with the number above and to the right, treating blank entries as 0.
For example, the initial number in the first (or any other) row is 1 (the sum of 0 and 1), whereas the numbers 1 and 3 in the third row are added to produce the number 4 in the fourth row.

     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1
In Pascal's triangle, each number is the sum of the two numbers directly above it.
"""

l = int(input("Enter l value: "))
n = int(input("Enter n value: "))

def generate_diagonal(n, l):
    # return an array containing the numbers in the nth diagonal of Pascal's triangle, to the specified length
    dict = {}
    dict[n] = []
    if l != 0:
        for i in range(n+1):
            dict[i] = [1]
        r = 0
        for i in range(n+1):
            for e in range(1,n+l-r):
                if i == 0:
                    dict[i].append(1)
                else:
                    dict[i].append(dict[i][e-1] + dict[i-1][e])
            r += 1
        return print(dict[n])
    else:
        return print(dict[n])

generate_diagonal(n, l)

"""
Alternative solutions:

def generate_diagonal(d, l):
    result = [1] if l else []
    for k in range(1, l):
        result.append(result[-1] * (d+k) // k)
    return result

def generate_diagonal(n, l):
    d = []
    for k in range(l):
        d.append(d[-1] * (n + k) // k if d else 1)
    return d

from scipy.special import comb
    def generate_diagonal(n, l):
        return [comb(n + a, a, exact=True) for a in range(l)]
"""

"""
Complete the function to determine the number of bits required to convert integer A to integer B (where A and B >= 0)

The upper limit for A and B is 216, int.MaxValue or similar.

For example, you can change 31 to 14 by flipping the 4th and 0th bit:

 31  0 0 0 1 1 1 1 1
 14  0 0 0 0 1 1 1 0
---  ---------------
bit  7 6 5 4 3 2 1 0
"""

a = int(input())
b = int(input())

def convert_bits(a, b):
    m = max(len('{0:b}'.format(a)), len('{0:b}'.format(b)))
    bit_a = "{0:{fill}{max}b}".format(a, fill='0', max = m)
    bit_b = "{0:{fill}{max}b}".format(b, fill='0', max = m)
    c = 0
    for i in range(m):
        if bit_a[i] != bit_b[i]:
            c += 1
    return c

print(convert_bits(a,b))

"""
Best solution:

def convert_bits(a,b):
    return bin(a^b).count("1")

Explanation:
Bitwise operator works on bits and performs bit by bit operation.
Assume if a = 60; and b = 13;
Now in binary format they will be as follows −

a = 0011 1100
b = 0000 1101
-----------------
a&b = 0000 1100
a|b = 0011 1101
a^b = 0011 0001
~a  = 1100 0011

& Binary AND
| Binary OR
^ Binary XOR
~ Binary Ones Complement
<< Binary Left Shift
>> Binary Right Shift
"""

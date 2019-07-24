"""
A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself.
Given a number, n, determine and print whether it's Prime or Not prime.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

def isprime(n):
    if n == 1:
        return 'Not prime'
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return 'Not prime'
    return 'Prime'

T = int(input())
for i in range(T):
    number = int(input())
    print(isprime(number))

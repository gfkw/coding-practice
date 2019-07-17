"""
Task
Write a Calculator class with a single method: int power(int,int). The power method takes two integers,n and p, as parameters and returns the integer result of n^p. If either n or p is negative, then the method must throw an exception with the message: n and p should be non-negative.
"""

#Write your code here

class Calculator:
    def power(self,n,p):
        self.n = n
        self.p = p
        if n < 0 or p < 0:
            raise Exception("n and p should be non-negative")
        else:
            return n**p

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        ans=power(n,p)
        print(ans)
    except Exception as e:
        print(e)

"""
Explanation:
In this program, "self" is used just for the convention purpose.
Inheriting the object class is not mandatory as in python it is considered as default.
Optionally: Since the method does not reference any class or instance attributes, you could make it a static method by using the @staticmethod decorator, which provides more flexibility by allowing you to call the method without creating a Calculator instance.
"""

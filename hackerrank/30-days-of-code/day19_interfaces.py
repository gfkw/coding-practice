"""
The AdvancedArithmetic interface and the method declaration for the abstract divisorSum(n) method are provided for you in the editor below.

Complete the implementation of Calculator class, which implements the AdvancedArithmetic interface.
The implementation for the divisorSum(n) method must return the sum of all divisors of n.
"""

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        return sum([i for i in range(1,n+1) if(n%i==0)])

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)

"""
Explanation 1:
Python doesn't support interfaces(and doesn't need to).
Python has powerful multiple inheritance anyways,
so languages like Java which have single inheritance only have to cope by inculcating "implementable" interfaces.

Explanation 2:
Because Python doesn't have (and doesn't need) a formal Interface contract, the Java-style distinction between abstraction and interface doesn't exist.
If someone goes through the effort to define a formal interface, it will also be an abstract class.
The only differences would be in the stated intent in the docstring.

And the difference between abstract and interface is a hairsplitting thing when you have duck typing.

Java uses interfaces because it doesn't have multiple inheritance.

Source: https://stackoverflow.com/questions/372042/difference-between-abstract-class-and-interface-in-python
"""

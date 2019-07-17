"""
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backwards and forwards.
Can you determine if a given string, s, is a palindrome?

To solve this challenge, we must first take each character in s, enqueue it in a queue, and also push that same character onto a stack.
Once that's done, we must dequeue the first character from the queue and pop the top character off the stack,
then compare the two characters to see if they are the same; as long as the characters match, we continue dequeueing,
popping, and comparing each character until our containers are empty (a non-match means S isn't a palindrome).
"""

import sys
from collections import deque

class Solution:
    # Write your code here
    def pushCharacter(self,char,stack):
        self.char = char
        self.stack = stack
        self.stack.append(self.char)

    def enqueueCharacter(self,char,queue):
        self.char = char
        self.queue = queue
        self.queue.append(self.char)

    def popCharacter(self,stack):
        self.stack = stack
        r = self.stack[-1]
        self.stack.pop()
        return r

    def dequeueCharacter(self,queue):
        self.queue = queue
        r = queue[0]
        self.queue.popleft()
        return r

queue = deque([])
stack = []
# read the string s
s=input()
#Create the Solution class object
obj=Solution()

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i], stack)
    obj.enqueueCharacter(s[i], queue)

isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
#print(queue, stack)
for i in range(l // 2):
    if obj.popCharacter(stack)!=obj.dequeueCharacter(queue):
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")

#print(queue, stack)

"""
Alternative solution:

class Solution:
    def __init__(self):
        self.mystack = list()
        self.myqueue = list()
        return(None)

    def pushCharacter(self, char):
        self.mystack.append(char)

    def popCharacter(self):
        return(self.mystack.pop(-1))

    def enqueueCharacter(self, char):
        self.myqueue.append(char)

    def dequeueCharacter(self):
        return(self.myqueue.pop(0))
"""

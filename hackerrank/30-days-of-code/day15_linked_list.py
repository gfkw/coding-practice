"""
Objective
A Node class is provided for you in the editor. A Node object has an integer data field, , and a Node instance pointer, , pointing to another node (i.e.: the next node in a list).
A Node insert function is also declared in your editor. It has two parameters: a pointer, , pointing to the first node of a linked list, and an integer  value that must be added to the end of the list as a new Node object.

Task
Complete the insert function in your editor so that it creates a new Node (pass  as the Node constructor argument) and inserts it at the tail of the linked list referenced by the  parameter. Once the new node is added, return the reference to the  node.
Note: If the  argument passed to the insert function is null, then the initial list is empty.
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
    #Complete this method
        if (head == None):
            head = Node(data)
        elif (head.next == None):
            head.next = Node(data)
        else:
            self.insert(head.next, data)
        return head

"""
- Explanation 1:
The function gets called with the whole linked list.
    If the list is empty,
    	insert the element as the head.
    Otherwise if there is no element after the head,
    	put the data after the head.
    Otherwise,
    	call the function with all of the elements except for the current head

- Explanation 2:
1. Head is returned as a reference or pointer to the next node.
2. With the help of head we'll traverse the complete list until we find the node (elif condition) which is pointing to the None or null.
3. The first if condition is executed only when the list is completely empty.
4. In this manner, recursive calls are made to insert function to reach the last node of the current list and then the passed data parameter is inserted there.
"""

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head);

# Stack implementation in python
# Author: Ricky Hewitt <ricky.hewitt@pm.me>

class Stack:
    """Stack ADT"""
    def __init__(self):
        self.data = []
    def pop(self):
        self.data.pop()
    def push(self, input):
        self.data.append(input)
    def read(self):
        return self.data[len(self.data)-1]
    def empty(self):
        self.data = []

# Test
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack.read()) # this should be 3
my_stack.pop()
print(my_stack.read()) # this should be 2
my_stack.push(4)
my_stack.push(5)
print(my_stack.read()) # this should be 5
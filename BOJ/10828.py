#pypy
import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
       
class Stack:
    def __init__(self):
        self._top = None
    
    def push(self, data):
        node = Node(data)
        
        if self._top == None:
            self._top = node
        else:
            node.next = self._top
            self._top = node
    
    def pop(self):
        if self._top == None:
            return -1
        
        value = self._top.data
        
        if self._top.next != None:
            self._top = self._top.next
        else:
            self._top = None
        
        return value

    def size(self):
        if self._top == None:
            return 0

        cur = self._top
        size = 1
        
        while cur.next != None:
            cur = cur.next
            size += 1
        
        return size
    
    def empty(self):
        return 1 if self._top == None else 0
        
    def top(self):
        if self._top == None:
            return -1
            
        return self._top.data
        

stack = Stack()
n = int(sys.stdin.readline())

for _ in range(n):
    command = sys.stdin.readline().split()
    
    if command[0] == "push":
        value = command[1]
        stack.push(value)
    elif command[0] == "pop":
        print(stack.pop())
    elif command[0] == "size":
        print(stack.size())
    elif command[0] == "empty":
        print(stack.empty())
    elif command[0] == "top":
        print(stack.top())


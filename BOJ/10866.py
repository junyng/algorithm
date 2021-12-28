# pypy3
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0
    
    def push_front(self, data):
        node = Node(data)
        
        if self.front == None:
            self.front = node
            self.rear = node
            self.count = 1
        else:
            self.front.next = node
            node.prev = self.front
            self.front = node
            self.count += 1
    
    def push_back(self, data):
        node = Node(data)
        
        if self.rear == None:
            self.rear = node
            self.front = node
            self.count = 1
        else:
            self.rear.prev = node
            node.next = self.rear
            self.rear = node
            self.count += 1
        
    def pop_front(self):
        if self.front == None:
            return -1
            
        value = self.front.data
        
        if self.front == self.rear:
            self.front = None
            self.rear = None
            self.count = 0
            return value
        
        self.front.prev.next = None
        self.front = self.front.prev
        self.count -= 1
        
        return value
        
    def pop_rear(self):
        if self.rear == None:
            return -1
            
        value = self.rear.data
        
        if self.front == self.rear:
            self.front = None
            self.rear = None
            self.count = 0
            return value
        
        self.rear.next.prev = None
        self.rear = self.rear.next
        self.count -= 1
        
        return value        
    
    def size(self):
        return self.count
    
    def empty(self):
        if self.rear == None:
            return 1
        else:
            return 0
    
    def _front(self):
        if self.front == None:
            return -1
        else:
            return self.front.data
            
    def _rear(self):
        if self.rear == None:
            return -1
        else:
            return self.rear.data

import sys

n = int(sys.stdin.readline())
deque = Deque()

for _ in range(n):
    string = sys.stdin.readline().split()
    command = string[0]
    
    if command == "push_front":
        number = string[1]
        deque.push_front(number)
    elif command == "push_back":
        number = string[1]
        deque.push_back(number)
    elif command == "pop_front":
        print(deque.pop_front())
    elif command == "pop_back":
        print(deque.pop_rear())
    elif command == "size":
        print(deque.size())
    elif command == "empty":
        print(deque.empty())
    elif command == "front":
        print(deque._front())
    elif command == "back":
        print(deque._rear())



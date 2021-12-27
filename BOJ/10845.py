#pypy3
import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Queue:
    def __init__(self):
        self._front = None
        self._rear = None
        
    def push(self, data):
        node = Node(data)
        
        if self._front == None:
            self._front = node
            self._rear = node
        else:
            self._rear.next = node
            self._rear = node
    
    def pop(self):
        if self._front == None:
            return -1
        
        value = self._front.data
        
        if self._front.next == None:
            self._front = None
            self._rear = None
        else:
            self._front = self._front.next
        
        return value
    
    def size(self):
        if self._front == None:
            return 0
        
        count = 1
        
        if self._front == self._rear:
            return count
        
        cur = self._front
        
        while cur.next != None:
            count += 1
            cur = cur.next
        
        return count
        
    def empty(self):
        if self._front == None:
            return 1
        else:
            return 0
    
    def front(self):
        if self._front == None:
            return -1
        
        return self._front.data
        
    def back(self):
        if self._rear == None:
            return -1
            
        return self._rear.data
        
queue = Queue()
n = int(sys.stdin.readline())

for _ in range(n):
    command = sys.stdin.readline().split()
    
    if command[0] == "push":
        value = command[1]
        queue.push(value)
    elif command[0] == "pop":
        print(queue.pop())
    elif command[0] == "size":
        print(queue.size())
    elif command[0] == "empty":
        print(queue.empty())
    elif command[0] == "front":
        print(queue.front())
    elif command[0] == "back":
        print(queue.back())

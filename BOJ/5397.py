# pypy3
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.start = Node('')
        self.pointer = self.start
    
    def add(self, data):
        node = Node(data)
        
        cur = self.pointer
        
        if cur.next != None:
            cur.next.prev = node
            node.next = cur.next
            node.prev = cur
        else:
            node.prev = cur
        
        cur.next = node
        
        self.pointer = node
            
    def remove(self):
        cur = self.pointer
        
        if cur.prev != None and cur.next != None:
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            self.pointer = cur.prev
        elif cur.prev != None and cur.next == None:
            cur.prev.next = None
            self.pointer = cur.prev
        elif cur.prev == None and cur.next != None:
            cur.next.prev = self.start
            self.start.next = cur.next
            self.pointer = self.start
        else:
            self.pointer = self.start
        
    def is_empty(self):
        return self.pointer == self.start
        
    def print_all(self):
        cur = self.start
        
        while True:
            print(cur.data, end='')
            if cur.next == None:
                break
            cur = cur.next
            
        print('')
    
    def backward(self):
        if self.pointer.prev != None:
            self.pointer = self.pointer.prev
        
    def forward(self):
        if self.pointer.next != None:
            self.pointer = self.pointer.next
            
n = int(input())

for _ in range(n):
    list = DoublyLinkedList()
    word = input()
    
    for c in word:
        if c == "<":
            list.backward()
        elif c == ">":
            list.forward()
        elif c == "-":
            list.remove()
        else:
            list.add(c)
    list.print_all()

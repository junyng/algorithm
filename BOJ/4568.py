import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class LRUCache:
    def __init__(self, size):
        self.head = Node('head')
        self.tail = Node('tail')
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = size
        self.count = 0
        self.lookup_table = {}
    
    # head에 둔다   
    def put(self, data):
        if data in self.lookup_table:
            node = self.lookup_table[data]
            self.remove(node)
            self.moveToEnd(node)
            return
        
        if self.count >= self.size:
            old = self.head.next
            del self.lookup_table[old.data]
            self.remove(old)
            self.count -= 1
        
        new = Node(data)
        self.lookup_table[data] = new
        self.moveToEnd(new)
        self.count += 1
    
    def remove(self, node):
        next = node.next
        prev = node.prev
        prev.next = next
        next.prev = prev
    
    def moveToEnd(self, node):
        prev_node_tail = self.tail.prev
        prev_node_tail.next = node
        node.prev = prev_node_tail
        node.next = self.tail
        self.tail.prev = node
    
    def description(self):
        cur = self.head.next
        while cur != self.tail:
            print(cur.data, end='')
            cur = cur.next
        print('')
        return

simulation_count = 1

while True:
    line = input()
    
    if line == '0':
        break
    
    n, string = line.split(' ')
    size = int(n)
    cache = LRUCache(size)
    
    print("Simulation %d" % simulation_count)
    
    for char in string:
        if char == "!":
            cache.description()
            continue
        
        cache.put(char)
    
    simulation_count += 1

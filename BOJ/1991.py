class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def pre_order(node):
    print(node.data, end='')
    if node.left != None:
        pre_order(tree[node.left])
    if node.right != None:
        pre_order(tree[node.right])

def in_order(node):
    if node.left != None:
        in_order(tree[node.left])
    print(node.data, end='')
    if node.right != None:
        in_order(tree[node.right])

def post_order(node):
    if node.left != None:
        post_order(tree[node.left])
    if node.right != None:
        post_order(tree[node.right])
    print(node.data, end='')

n = int(input())

tree = {}

for _ in range(n):
    data, left, right = input().split()
    node = Node(data)
    if left != '.':
        node.left = left
    if right != '.':
        node.right = right
    tree[data] = node

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])

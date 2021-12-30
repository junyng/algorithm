n = int(input())

left = None
right = None
area = 0

nodes = list()

for _ in range(n):
    node = list(map(int, input().split()))
    nodes.append(node)

nodes.sort(key = lambda node : node[0])

for l, h in nodes:
    if left == None:
        left = l, h
        continue
    
    pl, ph = left
    
    if ph < h:
        size = (l - pl) * ph
        area += size
        left = l, h

for l, h in reversed(nodes):
    if right == None:
        right = l, h
        continue
    
    pl, ph = right
    
    if ph < h:
        size = (pl - l) * ph
        area += size
        right = l, h

area += ((right[0] - left[0]) + 1) * right[1]

print(area)

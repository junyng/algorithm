import sys
from collections import deque

classmates = [deque() for i in range(22)]
n, k = map(int, sys.stdin.readline().split())

count = 0

for score in range(n):
    name = sys.stdin.readline()
    names = classmates[len(name)]
    
    while True:
        if not names:
            names.append((name, score))
            break
        
        if score - names[0][1] > k:
            names.popleft()
        else:
            count += len(names)
            names.append((name, score))
            break

print(count)

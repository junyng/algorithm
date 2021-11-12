from collections import deque

n, m = map(int, input().split())

adj = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

dist = [0] * (n + 1)
visited = [False] * (n + 1)

def bfs(adj, visited, start):
    visited[start] = True
    queue = deque([start])
    d = 0
    
    while queue:
        group = len(queue)
        d += 1
        
        for _ in range(group):
            v = queue.popleft()
            
            for i in adj[v]:
                if not visited[i]:
                    visited[i] = True
                    dist[i] = d
                    queue.append(i)

bfs(adj, visited, 1)

items = dict()

for i, d in enumerate(dist):
    number = i
    
    if d in items:
        items[d].append(number)
    else:
        items[d] = [number]

distance = max(items.keys())
pos = min(items[distance])
count = len(items[distance])

print(pos, distance, count)


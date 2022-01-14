from collections import deque
from collections import defaultdict

def bfs(graph, node):
    visited = list()
    queue = deque([node])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
            print(node, end=' ')

def dfs(graph, node):
    visited = list()
    stack = list([node])
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))
            print(node, end= ' ')

graph = defaultdict(list)

n, m, node = map(int, input().split())

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for key in graph.keys():
    graph[key].sort()

dfs(graph, node)
print()
bfs(graph, node)

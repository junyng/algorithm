N = int(input())
M = int(input())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split(' '))))

cities = list(map(int, input().split(' ')))

start = cities[0] - 1

visited = [False] * N

queue = [start]

while queue:
    city = queue.pop(0)
    visited[city] = True
    
    for i in range(N):
        if graph[city][i] and not visited[i]:
            queue.append(i)
            visited[i] = True

for city in cities:
    if not visited[city - 1]:
        print("NO")
        exit(0)
    
print("YES")

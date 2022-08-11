from sys import stdin

N, M = map(int, stdin.readline().split())
count = 0

graph = [[] for _ in range(N + 1)]

for i in range(N-1):
    U, V = map(int, stdin.readline().split())
    
    graph[U].append(V)
    graph[V].append(U)
    
for i in range(2, N+1):
    if len(graph[i]) == 1:
        count += 1

print(M / count)

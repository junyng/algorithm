from collections import deque

n = int(input())
dirs = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]

def coords(visited, x, y):
    coords = []
    
    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy
        
        if 0 <= nx < len(visited) and 0 <= ny < len(visited) and not visited[nx][ny]:
            visited[nx][ny] = True
            coords.append((nx, ny))
    
    return coords

for _ in range(n):
    # input
    l = int(input())
    x, y = map(int, input().split())
    tx, ty = map(int, input().split())
    
    visited = [[False for _ in range(l)] for _ in range(l)]
    visited[x][y] = True
    dist = [[0 for _ in range(l)] for _ in range(l)]
    
    queue = deque([(x, y)])
    
    while queue:
        x, y = queue.popleft()
        if x == tx and y == ty:
            print(dist[x][y])
            break
        
        for nx, ny in coords(visited, x, y):
            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny))

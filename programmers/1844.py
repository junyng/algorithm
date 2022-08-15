from collections import deque

def solution(maps):
    answer = 0
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    queue = deque([(0, 0, 1)])
    
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    
    visited[0][0] = True
    
    while queue:
        cur = queue.popleft()
        
        if cur[0] == n - 1 and cur[1] == m - 1:
            return cur[2]
    
        for i in range(4):
            nx = dx[i] + cur[0]
            ny = dy[i] + cur[1]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny, cur[2] + 1))
                
    return -1

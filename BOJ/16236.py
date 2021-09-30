from heapq import heappush, heappop

def bfs(time, shark):
    size, count, total_time = 2, 0, 0
    heap = []
    heappush(heap, (time, shark[0], shark[1]))
    visited = [[False] * n for _ in range(n)]
    
    while heap:
        time, x, y = heappop(heap)
        
        if 0 < board[x][y] < size:
            count += 1
            board[x][y] = 0
            
            if count == size:
                size += 1
                count = 0
                
            total_time += time
            time = 0
            heap = []
            visited = [[False] * n for _ in range(n)]
        
        for i in range(4):
            moved_x = dx[i] + x
            moved_y = dy[i] + y
            
            if 0 <= moved_x < n and 0 <= moved_y < n and board[moved_x][moved_y] <= size and not visited[moved_x][moved_y]:
                visited[moved_x][moved_y] = True
                heappush(heap, (time + 1, moved_x, moved_y))
    
    return total_time
    
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0 ,-1, 0]
    
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            board[i][j] == 0
            print(bfs(0, [i, j]))
            

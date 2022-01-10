from collections import deque
import sys

readline = sys.stdin.readline

n, m = map(int, readline().split())
board = []

for i in range(n):
    board.append(list(readline()))
    for j in range(m):
        if board[i][j] == 'R':
            ry, rx = i, j
        elif board[i][j] == 'B':
            by, bx = i, j

queue = deque([(ry, rx, by, bx)])
visited = [(ry, rx, by, bx)]

moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
count = 0

while queue:
    if count > 10:
        break
    
    for _ in range(len(queue)):
        ry, rx, by, bx = queue.popleft()
    
        if board[ry][rx] == 'O' and board[by][bx] != 'O':
            print(count)
            exit(0)
    
        for dy, dx in moves:
            nry = ry
            nrx = rx
            nby = by
            nbx = bx
        
            while True:
                if board[nry][nrx] != '#' and board[nry][nrx] != 'O':
                    nry += dy
                    nrx += dx
                else:
                    if board[nry][nrx] == '#':
                        nry -= dy
                        nrx -= dx
                    break
            
            while True:
                if board[nby][nbx] != '#' and board[nby][nbx] != 'O':
                    nby += dy
                    nbx += dx
                else:
                    if board[nby][nbx] == '#':
                        nby -= dy
                        nbx -= dx
                    break
            
            if board[nby][nbx] == 'O':
                continue
        
            if nry == nby and nrx == nbx:
                if abs(nry - ry) + abs(nrx - rx) > abs(nby - by) + abs(nbx - bx):
                    nry -= dy
                    nrx -= dx
                else:
                    nby -= dy
                    nbx -= dx
        
            if (nry, nrx, nby, nbx) not in visited:
                queue.append((nry, nrx, nby, nbx))
                visited.append((nry, nrx, nby, nbx))
    
    count += 1
    
print(-1)

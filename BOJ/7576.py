from collections import deque

def find(board, number):
    width = len(board[0])
    height = len(board)
    pos = []
    
    for y in range(width):
        for x in range(height):
            if board[x][y] == number:
                pos.append((x, y))
    
    return pos


dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

m, n = map(int, input().split(' '))

missed = set()

board = []

for _ in range(n):
    board.append(list(map(int, input().split(' '))))


pos = deque(find(board, 1))
time = -1

while pos:
    step_size = len(pos)
    time += 1
    for _ in range(step_size):
        x, y = pos.popleft()
        for d in dirs:
            nx, ny = x+d[0], y+d[1]
            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if board[nx][ny] == 0:
                    board[nx][ny] = 1
                    pos.append((nx, ny))

if len(find(board, 0)) > 0:
    print(-1)
else:
    print(time)

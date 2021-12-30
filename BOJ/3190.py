from collections import deque

n = int(input())
k = int(input())

board = [[-1 for i in range(n)] for i in range(n)]

for _ in range(k):
    y, x = map(int, input().split())
    board[y-1][x-1] = 0

rotation = dict()
l = int(input())
for _ in range(l):
    time, rotate = input().split()
    rotation[int(time)] = rotate

moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# start
direction = 0
time = 1
y, x = 0, 0
queue = deque()
queue.append((y, x))
board[y][x] = 1

while True:
    dy, dx = moves[direction]
    y, x = y + dy, x + dx
    
    if 0 <= y < n and 0 <= x < n and board[y][x] != 1:
        if not board[y][x] == 0:
           ty, tx = queue.popleft()
           board[ty][tx] = -1
        board[y][x] = 1
        queue.append((y, x))
        if time in rotation:
            if rotation[time] == "L":
                direction = (direction - 1) % len(moves)
            elif rotation[time] == "D":
                direction = (direction + 1) % len(moves)
        time += 1
    else:
        break

print(time)

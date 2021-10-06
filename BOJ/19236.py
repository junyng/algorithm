import copy

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def leftover(board, x, y):
    positions = []
    direction = board[x][y][1]
    for i in range(1, 4):
        nx, ny = x + dx[direction], y + dy[direction]
        if 0 <= nx < 4 and 0 <= ny < 4 and 1 <= board[nx][ny][0] <= 16:
            positions.append([nx, ny])
        x, y = nx, ny
    return positions
    
def find_fish(board, index):
    for x in range(4):
        for y in range(4):
            if board[x][y][0] == index:
                return (x, y)
    return None
    
def move_fishes(board, shark_x, shark_y):
    for i in range(1, 17):
        pos = find_fish(board, i)
        if pos == None: continue
        x, y = pos
        dir = board[x][y][1]
    
        for i in range(8):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < 4 and 0 <= ny < 4 and not (nx == shark_x and ny == shark_y):
                board[x][y][0], board[nx][ny][0] = board[nx][ny][0], board[x][y][0]
                board[x][y][1], board[nx][ny][1] = board[nx][ny][1], dir
                break
            dir = (dir + 1) % 8

def dfs(board, x, y, total):
    global answer
    board = copy.deepcopy(board)
    
    number = board[x][y][0]
    board[x][y][0] = -1
    
    move_fishes(board, x, y)
    
    positions = leftover(board, x, y)
    
    answer = max(answer, total + number)
    
    for x, y in positions:
        dfs(board, x, y, total + number)
    

arr = [list(map(int, input().split())) for _ in range(4)]
board = [[None] * 4 for _ in range(4)]
for i in range(4):
    for j in range(4):
        board[i][j] = [arr[i][j * 2], arr[i][j * 2 + 1] - 1]
answer = 0
dfs(board, 0, 0, 0)
print(answer)

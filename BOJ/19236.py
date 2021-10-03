answer = 0

result = []
fishes = {}
board = {}
moves = {1:-4, 2: -3, 3:1, 4:5, 5:4, 6:3, 7:-1, 8:-5}


for j in range(4):
    row = list(map(int, input().split()))
    for i in range(1, len(row)+1, 2):
        number = row[i-1]
        direction = row[i]
        pos = (i // 2 + 1) + j * 4
        fishes[number] = (pos, direction) 
        board[pos] = number


def dfs(i, r, eat, board, fishes):
    if r == 17:
        result.append(eat)
        return
    
    if board[i] != -1:
        eat += board[i]
        
    board[i] = -1
    direction = fishes[i][1]
        
    move = moves[direction]
    next_i = i + move
    
    while (1 <= next_i <= 16):
        board[i] = 0
        move_fishes(board, fishes)
        dfs(next_i, r+1, eat, board, fishes)
        next_i += move
    else:
        move_fishes(board, fishes)
        dfs(i, r+1, eat, board, fishes)


def move_fishes(board, fishes):
    for j in range(1, 16):
        if j in fishes:
            fish = fishes[j]
            source = fish[0]
            direction = fish[1]
            move = moves[direction]
            target = source + move
            if 1 <= target <= 16 and board[target] != -1:
                board[source], board[target] = board[target], board[source]

dfs(1, 1, 0, board, fishes)
print(result)

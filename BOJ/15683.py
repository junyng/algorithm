from itertools import product

def check(visited, x, y, d):
    
    if 0 > x or x >= n:
        return
    
    if 0 > y or y >= m:
        return
    
    if data[x][y] == '6':
        return   
    
    visited[x][y] = True
    
    if d == 0:
        check(visited, x, y-1, d)
    elif d == 2:
        check(visited, x, y+1, d)
    elif d == 1:
        check(visited, x+1, y, d)
    elif d == 3:
        check(visited, x-1, y, d)


n, m = map(int, input().split())
directions = {'1': [[0], [1], [2], [3]],
              '2': [[0, 2], [1, 3]],
              '3': [[0, 1], [1, 2], [2, 3], [3, 0]],
              '4': [[3, 0, 1], [0, 1, 2], [1, 2, 3]],
              '5': [[0, 1, 2, 3]]
}

data = []
commands = []

for i in range(n):
    data.append(list(map(int, input().split())))
    
for i in range(n):
    for j in range(m):
        if 0 < data[i][j] and data[i][j] < 6:
            commands.append(directions[str(data[i][j])])

visited = [[False]*m for _ in range(n)]

# print(commands)
for p in product(commands):
    print(p)

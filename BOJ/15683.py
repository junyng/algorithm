from itertools import product

def check(visited, x, y, d):
    
    if 0 > x or x >= n:
        return
    
    if 0 > y or y >= m:
        return
    
    if data[x][y] == 6:
        visited[x][y] = True
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
              '4': [[3, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 0]],
              '5': [[0, 1, 2, 3]]
}

data = []
commands = []
pos = []

for i in range(n):
    data.append(list(map(int, input().split())))
    
for i in range(n):
    for j in range(m):
        if 0 < data[i][j] and data[i][j] < 6:
            command = directions[str(data[i][j])]
            commands.append(command)
            pos.append((i, j))

visited = [[False]*m for _ in range(n)]

product = list(product(*commands))

result = -1

for p in product:
    visited = [[False]*m for _ in range(n)]
    for i in range(len(p)):
        for c in range(len(p[i])):
            check(visited, pos[i][0], pos[i][1], p[i][c])
            
    count = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == False and data[i][j] != 6:
                count += 1
    
    if result == -1:
        result = count
        
    if result > count:
        result = count
        
print(result)

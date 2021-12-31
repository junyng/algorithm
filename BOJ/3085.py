n = int(input())

moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

board = [list(input()) for _ in range(n)]

answer = 1

for y in range(n):
    for x in range(n):
        
        # x
        prev = board[y][0]
        index = 1
        count = 1
                
        while(index < n):
            if prev == board[y][index]:
                count += 1
                answer = max(answer, count)
            else:
                prev = board[y][index]
                count = 1
            index += 1
        
        # y
        prev = board[0][x]
        index = 1
        count = 1
                
        while(index < n):
            if prev == board[index][x]:
                count += 1
                answer = max(answer, count)
            else:
                prev = board[index][x]
                count = 1
            index += 1
                

        for dy, dx in moves:
            ny = y + dy
            nx = x + dx
            
            if 0 <= ny < n and 0 <= nx < n:
                board[y][x], board[ny][nx] = board[ny][nx], board[y][x]
                # count
                prev = board[y][0]
                index = 1
                count = 1
                
                while(index < n):
                    if prev == board[y][index]:
                        count += 1
                        answer = max(answer, count)
                    else:
                        prev = board[y][index]
                        count = 1
                    index += 1
                
                prev = board[0][x]
                index = 1
                count = 1
                
                while(index < n):
                    if prev == board[index][x]:
                        count += 1
                        answer = max(answer, count)
                    else:
                        prev = board[index][x]
                        count = 1
                    index += 1
                
                board[y][x], board[ny][nx] = board[ny][nx], board[y][x]

print(answer)

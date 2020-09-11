#pypy 제출
import sys

def dfs(d, r, c):
    global count
    
    if r == n-1 and c == n-1:
        count+=1
        return
    
    if d == 0 or d == 2:
        if c+1 < n:
            if m[r][c+1] == 0:
                dfs(0, r, c+1)
    if d == 1 or d == 2:
        if r+1 < n:
            if m[r+1][c] == 0:
                dfs(1, r+1, c)
    if d == 0 or d == 1 or d == 2:
        if c+1 < n and r+1 < n:
            if m[r][c+1] == 0 and m[r+1][c] == 0 and m[r+1][c+1] == 0:
                dfs(2, r+1, c+1)
input = sys.stdin.readline
count = 0
n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
dfs(0, 0, 1)
print(count)

def dfs(n, cur, computers, visited):
    visited[cur] = True
    
    for i in range(n):
        if computers[cur][i] == 1 and i != cur and not visited[i]:
            dfs(n, i, computers, visited)


def solution(n, computers):
    visited = [False] * n
    count = 0
    
    for i in range(n):
        if not visited[i]:
            dfs(n, i, computers, visited)
            count += 1
    
    return count

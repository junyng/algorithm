def dfs(l):
    if l == n:
        print(' '.join(result))
        return
    
    for i in range(n):
        if check[i] == 0:
            result[l] = str(array[i])
            check[i] = 1
            dfs(l+1)
            check[i] = 0

n = int(input())
array = [i for i in range(1, n+1)]
result = [0] * n
check = [0] * n
dfs(0)

n, m = map(int, input().split(" "))
c = [False] * (n+1)
a = [0] * m

def go(index, start, n, m):
    if index == m:
        print(' '.join(map(str, a)))
        return
    
    for i in range(start, n+1):
        c[i] = True
        a[index] = i
        go(index + 1, i, n, m)
        c[i] = False

go(0, 1, n, m)

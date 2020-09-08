def rotate_left(l):
    first = l[0]
    for i in range(1, len(l)):
        l[i-1] = l[i]
    
    l[len(l) - 1] = first
    
def rotate_right(l):
    last = l[7]
    for i in range(6, -1, -1):
        l[i+1] = l[i]
    
    l[0] = last

def rotate(i, d):
    if not visited[i]:
        visited[i] = True
        left = data[i][6]
        right = data[i][2]
    
        if d == 1:
            rotate_right(data[i])
        else:
            rotate_left(data[i])
        
        if i > 0 and left != data[i-1][2]:
            rotate(i-1, -d)
        if i < 3 and right != data[i+1][6]:
            rotate(i+1, -d)

data = []

for i in range(4):
    data.append(list(input()))

n = int(input())

result = 0

for i in range(n):
    s, d = map(int, input().split())
    visited = [False] * 4
    rotate(s-1, d)
    
result = 0

for i in range(4):
    if data[i][0] == '1':
        result += (2**i)
        
print(result)

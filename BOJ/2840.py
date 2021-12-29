n, k = map(int, input().split())
papers = ['?' for i in range(n)]
index = 0
check = True

for _ in range(k):
    s, c = input().split()
    index = (index + int(s)) % n
    
    if papers[index] == '?':
        papers[index] = c
    else: 
        if papers[index] != c:
            check = False
            break

for i in range(n):
    base = papers[i]
    for j in range(i+1, n):
        target = papers[j]
        
        if base == target and base != '?':
            check = False

if check:
    for _ in range(n):
        print(papers[index], end='')
        index = (index - 1) % n
else:
    print("!")

from collections import deque

n = int(input())
queue = deque()
balloons = list(enumerate(map(int, input().split())))

for balloon in balloons:
    queue.append(balloon)

for i in range(n):
    number, move = queue.popleft()
    if i == n-1:
        print(number+1, end='')
    else:
        print(number+1, end=' ')
    if move > 0:
        queue.rotate(-(move-1))
    else:
        queue.rotate(-move)

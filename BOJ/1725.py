n = int(input())

stack = list()

area = 0

rects = [int(input()) for i in range(n)]

for index in range(n):
    while stack and rects[stack[-1]] > rects[index]:
        rect = rects[stack[-1]]
        stack.pop()
        dist = index
        if stack:
            dist -= stack[-1] + 1
        area = max(area, rect * dist)
    stack.append(index)
    
while stack:
    rect = rects[stack[-1]]
    stack.pop()
    dist = n
    if stack:
        dist -= stack[-1] + 1
    area = max(area, rect * dist)
    
print(area)

stack = list()

n = int(input())

count = 0

for _ in range(n):
    word = input()
    stack = list()
    
    is_good = True
    
    for char in word:
        if not stack:
            stack.append(char)
        else:
            if stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
    
    if not stack and is_good:
        count += 1

print(count)

from collections import deque

T = int(input())

for _ in range(T):
    commands = list(input())
    n = int(input())
    string = input()[1:-1]
    array = string.split(",") if len(string) > 0 else []
    queue = deque(array)
    count = 0
    
    is_valid = True
    
    for command in commands:
        
        if command == "R":
            count += 1
        elif command == "D":
            if len(queue) < 1:
                is_valid = False
                break
            
            queue.popleft() if count % 2 == 0 else queue.pop()
    
    if count % 2 != 0:
        queue.reverse()
    
    if is_valid:
        print('[', end='')
        print(','.join(queue), end='')
        print(']')
    else:
        print("error")

n, m = map(int, input().split())
commands = list()

train = [0] * n

for _ in range(m):
    command = list(map(int, input().split()))
    index = command[1] - 1
    
    if command[0] == 1:
        train[index] = train[index] | (1 << (command[2] - 1))
    elif command[0] == 2:
        train[index] = (train[index] | (1 << (command[2] - 1) )) ^ (1 << (command[2] - 1))
    elif command[0] == 3:
        train[index] = (train[index] << 1) & ((1 << 20) - 1)
    elif command[0] == 4:
        train[index] = train[index] >> 1
        
print(len(set(train)))

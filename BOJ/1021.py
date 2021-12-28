n, m = map(int, input().split())
targets = list(map(int, input().split()))

numbers = [i for i in range(1, n+1)]

pointer = 0
count = 0

for target in targets:
    for i in range(len(numbers)):
        index = (pointer + i) % len(numbers)
        
        if numbers[index] == target:
            pointer = index
            
            if i * 2 > len(numbers):
                count += (len(numbers) - i)
            else:
                count += i
            del numbers[index]
            break
        
print(count)

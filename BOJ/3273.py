n = int(input())
arr = sorted(list(map(int, input().split())))
target = int(input())

start = 0
end = n-1
count = 0

while(start != end):
    first = arr[start]
    second = arr[end]
    value = first + second
    
    if value < target:
        start += 1
    elif value > target:
        end -= 1
    else:
        count += 1
        start += 1
        
print(count)
        

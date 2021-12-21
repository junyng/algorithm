n, s = map(int, input().split())
numbers = list(map(int, input().split()))

start = 0
end = 0

answer = n + 1
partial_sum = 0

while True:
    if partial_sum >= s:
        partial_sum -= numbers[start]
        answer = min(end - start, answer)
        start += 1
    elif end == n:
        break
    else:
        partial_sum += numbers[end]
        end += 1

if answer == n + 1:
    print(0)
else:
    print(answer)

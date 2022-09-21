n = int(input())
numbers = list(map(int, input().split()))

results = [0] * n

results[0] = numbers[0]

for i in range(1, n):
    results[i] = max(numbers[i], numbers[i] + results[i-1])

print(max(results))

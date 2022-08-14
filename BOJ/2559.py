N, K = map(int, input().split(' '))
numbers = list(map(int, input().split(' ')))

results = [sum(numbers[:K])]

for i in range(len(numbers) - K):
    result = results[-1] - numbers[i] + numbers[i + K]
    results.append(result)
    
print(max(results))

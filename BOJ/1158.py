n, k = map(int, input().split())
numbers = [n for n in range(1, n + 1)]
result = []

index = 0

while(numbers):
    index = (index + k - 1) % len(numbers)
    result.append(str(numbers.pop(index)))

print("<", ", ".join(result), ">", sep="")

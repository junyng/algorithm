numbers = input()
result = int(numbers[0])

for number in numbers[1:]:
    number = int(number)
    if number <= 1 or result <= 1:
        result += number
    else:
        result *= number
        
print(result)

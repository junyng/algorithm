def calculate(x, y, op):
    return eval(str(x)+op+str(y))

def operate(i, value):
    global result
    
    if i >= len(operators):
        result = max(result, value)
        return
    
    operate(i+1, calculate(value, numbers[i+1], operators[i]))
    
    if i+1 < len(operators):
        nextValue = calculate(numbers[i+1], numbers[i+2], operators[i+1])
        operate(i+2, calculate(value, nextValue, operators[i]))
        
result = float('-inf')
n = int(input())
exp = list(input())

numbers = []
operators = []

for i in range(n):
    if i % 2 == 0:
        numbers.append(int(exp[i]))
    else:
        operators.append(exp[i])
        

operate(0, numbers[0])
print(result)

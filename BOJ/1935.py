import string

numbers = dict()
operators = ["*", "/", "+", "-"]
    
n = int(input())
expr = input()
stack = list()

for ascii in range(65, 65 + n):
    numbers[chr(ascii)] = int(input())

for char in expr:
    # 1. 피연산자이면 스택에 push
    if char not in operators:
        stack.append(numbers[char])
    # 2. 연산자이면 스택의 가장 위의 값 2개를 꺼내 연산한 결과를 스택에 push
    else:
        operand2 = stack.pop()
        operand1 = stack.pop()
        result = eval(str(operand1) + char + str(operand2))
        stack.append(result)

print('%.2f' % stack.pop())

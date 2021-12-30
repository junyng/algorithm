expr = list(input())
stack = list()

# operator with priority
operators = {
    "*": 2,
    "/": 2, 
    "+": 1, 
    "-": 1
}

while expr:
    char = expr.pop(0)
    
    # 1. 피연산자를 만나면 출력한다.
    if char.isalnum():
        print(char, end='')
        continue
    
    # 2. 사칙연산자를 만나면
    # 스택이 비어있거나, top이 여는 괄호이거나, 이번 연산자 우선순위가 top 연산자보다 높으면 push
    # 그렇지 않으면 조건을 만족할 때까지 pop
    
    if char in operators:
        # 비어있으면
        while True:
            if not stack:
                stack.append(char)
                break
            elif stack[-1] == "(":
                stack.append(char)
                break
            elif stack[-1] in operators and operators[char] > operators[stack[-1]]:
                stack.append(char)
                break
            else:
                print(stack.pop(), end='')
        continue
    
    # 3. 여는 괄호를 만나면 push, 닫힌 괄호를 만나면 (가 나올때까지 pop
    if char == "(":
        stack.append(char)
        continue
    elif char == ")":
        while stack[-1] != "(":
            print(stack.pop(), end='')
        stack.pop()
        continue
    
while stack:
    print(stack.pop(), end='')

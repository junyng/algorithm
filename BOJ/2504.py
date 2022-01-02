def check(string):
    stack = []
    
    for char in string:
        if char in ["(", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            else:
                bracket = stack.pop()
                
                if bracket == "(" and char == ")":
                    continue
                elif bracket == "[" and char == "]":
                    continue
                else:
                    return False
    
    if stack:
        return False
    
    return True

string = input()

if not check(string):
    print(0)
    exit(0)

open_brackets = {
    "(": 2,
    "[": 3
}

close_brackets = {
    ")": 2,
    "]": 3
}

stack = []
result = 0
partial_sum = 1

for index, char in enumerate(string):
    if char in open_brackets:
        
        stack.append(char)
        
        weight = open_brackets[char]
        partial_sum *= weight
        
        if index + 1 < len(string) and string[index+1] in close_brackets:
            result += partial_sum
    
    else:
        weight = close_brackets[char]
        partial_sum //= weight
        if stack[-1] in open_brackets:
            stack.pop()

print(result)

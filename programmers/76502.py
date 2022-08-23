def check(s):
    matches = {'(': ')', '[': ']', '{': '}'}
    stack = []
    
    for char in s:
        if char == "(" or char == "[" or char == "{":
            stack.append(char)
        else:
            if not stack:
                return 0
            if matches[stack.pop()] != char:
                return 0
    if len(stack) > 0:
        return 0
        
    return 1

def solution(s):
    count = 0
    
    for i in range(len(s)):
        count += check(s[i:] + s[:i])
    
    return count

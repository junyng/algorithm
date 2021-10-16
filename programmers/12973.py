def solution(s):
    stack = []
    
    for c in s:
        if stack:
            if c == stack[-1]:
                stack.pop()
                continue
        stack.append(c)
        
    answer = 0 if stack else 1
    
    return answer

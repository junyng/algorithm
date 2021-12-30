import sys

lines = sys.stdin.readlines()

for line in lines[:-1]:
    start = 0
    stack1 = list()
    stack2 = list()
    
    while start < len(line):
        if line[start] == "<":
            is_opening = True
            if line[start+1] == "/":
                start += 1
                is_opening = False
            
            end = start + 1
            
            while line[end] != ">":
                if line[end] == " ":
                    break
                end += 1
                
            tag = line[start+1:end]
            
            if tag != 'br':
                if is_opening:
                    stack1.append(tag)
                else:
                    stack2.append(tag)
                
        start += 1

    is_legal = True
    
    if len(stack1) != len(stack2):
        is_legal = False
    else:
        while stack2:
            closing = stack2.pop(0)
            opening = stack1.pop()
            
            if closing != opening:
                is_legal = False
                break
    
    if is_legal:
        print("legal")
    else:
        print("illegal")

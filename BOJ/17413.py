S = input()

stack = []
is_tag = False

for char in S:
    if char == '>':
        stack.append(char)
        print(''.join(stack), end='')
        stack = []
        is_tag = False
        continue
    
    if char == '<':
        print(''.join(stack[::-1]), end='')
        stack = []
        stack.append(char)
        is_tag = True
        continue
    
    if char == ' ' and not is_tag:
        print('{} '.format(''.join(stack[::-1])), end='')
        stack = []
        continue
    
    stack.append(char)

print(''.join(stack[::-1]))

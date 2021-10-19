def validate(string):
    stack = []
    for char in string:
        if char == '(':
            stack.append(char)
        elif stack:
            stack.pop()
    return not stack

def solution(string):
    # 1. 빈 문자열 검사
    if string == '':
        return ''
    # 2. 문자열을 u, v로 분리
    queue = list(string)
    u = ''
    cur = 0
    while queue:
        u += queue.pop(0)
        if u[-1] == '(':
            cur += 1
        else:
            cur -= 1
        if cur == 0:
            break
    v = ''.join(queue)
    # 3. 올바른 괄호 문자열 수행
    if validate(u):
        return u + solution(v)
    # 4. 문자열 반환
    remain = ''.join([')' if char == '(' else '(' for char in u[1:-1]])
    return '(' + solution(v) + ')' + remain

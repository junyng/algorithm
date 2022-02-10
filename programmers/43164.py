from collections import defaultdict

def solution(tickets):
    paths = defaultdict(list)
    
    for src, dst in tickets:
        paths[src].append(dst)
        
    for key in paths.keys():
        paths[key].sort(reverse=True)
    
    answer = []
    stack = [tickets[0][0]]
    
    while stack:
        src = stack[-1]
        
        if not paths[src]:
            answer.append(stack.pop())
        else:
            stack.append(paths[src].pop())
    
    answer.reverse()
        
    return answer

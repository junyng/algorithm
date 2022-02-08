def is_convertible(base, target):
    count = 0
    
    for i in range(len(base)):
        if base[i] != target[i]:
            count += 1
            
    if count == 1:
        return True
    else:
        return False

def bfs(begin, target, words, visited):
    count = 0
    
    stack = [(begin, 0)]
    
    while stack:
        word, level = stack.pop()
        
        if word == target:
            return level
            
        for i in range(len(words)):
            if visited[i]: continue
        
            if is_convertible(word, words[i]):
                visited[i] = True
                stack.append((words[i], level+1))

def solution(begin, target, words):
    if target not in words:
        return 0
        
    visited = [False] * len(words)
    
    answer = bfs(begin, target, words, visited)
    
    return answer

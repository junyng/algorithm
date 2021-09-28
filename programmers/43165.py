def dfs(numbers, target, value, index):
    global answer
    if index >= len(numbers):
        if target == value:
            answer += 1
        return
    dfs(numbers, target, value+numbers[index], index+1)
    dfs(numbers, target, value-numbers[index], index+1)

def solution(numbers, target):
    global answer
    answer = 0
    
    dfs(numbers, target, 0, 0)
    return answer

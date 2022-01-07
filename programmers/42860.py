def solution(name):
    moves = [min(ord(char) - ord('A'), ord('Z') - ord(char) + 1) for char in name]
    index = 0
    answer = 0
    
    while True:
        answer += moves[index]
        moves[index] = 0
        if sum(moves) == 0:
            break
        left, right = 1, 1
        while moves[index - left] == 0:
            left += 1
        while moves[index + right] == 0:
            right += 1
        
        if left < right:
            answer += left
            index -= left
        else:
            answer += right
            index += right
    
    return answer

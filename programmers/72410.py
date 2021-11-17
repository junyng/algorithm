def solution(new_id):
    answer = ''
    # 1, 2
    for char in new_id:
        if char.isupper():
            answer += char.lower()
        elif char.isalnum() or char == "-" or char == "_":
            answer += char
        elif char == ".":
            if answer and answer[-1] == char:
                continue
            else:
                answer += char
    
    answer = answer.strip(".")
    # 5
    if not answer:
        answer = "a"
        
    # 6
    if len(answer) >= 16:
        answer = answer[:15].rstrip(".")
    
    # 7
    while(len(answer) <= 2):
        answer += answer[-1]
    
    return answer

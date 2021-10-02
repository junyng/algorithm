def solution(record):
    answer = []
    users = {}
    
    for action in record:
        items = action.split(' ')
        command = items[0]
        if command == "Enter":
            users[items[1]] = items[2]
        elif command == "Change":
            users[items[1]] = items[2]
    
    
    for action in record:
        items = action.split(' ')
        command = items[0]
        if command == "Change":
            continue
        elif command == "Enter":
            answer.append("%s님이 들어왔습니다."% users[items[1]])
        elif command == "Leave":
            answer.append("%s님이 나갔습니다."% users[items[1]])
    return answer

from collections import defaultdict

def solution(id_list, reports, k):
    record = set()
    
    for report in reports:
        user, other = report.split(' ')
        record.add((user, other))
    
    result = defaultdict(list)
    
    for user, other in list(record):
        result[other].append(user)
    
    users = defaultdict(int)
    
    for id in id_list:
        users[id] = 0
        
    for reported, reporters in result.items():
        if len(reporters) >= k:
            for reporter in reporters:
                users[reporter] += 1
    
    notice_counts = list(map(lambda i: users[id_list[i]], range(len(id_list))))
    return notice_counts

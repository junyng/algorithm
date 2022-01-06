def solution(peoples, limit):
    peoples.sort()
    count = 0
    start, end = 0, len(peoples) - 1
    
    while(start<end):
        if peoples[start] + peoples[end] <= limit:
            count += 1
            start += 1
            end -= 1
        else:
            end -= 1
            count += 1
    if start == end:
        count += 1
    return count

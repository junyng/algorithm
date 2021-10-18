def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n
    
    while left < right:
        mid = (left + right) // 2
        people = 0
        
        for time in times:
            people += mid // time
            
        if people >= n:
            right = mid
        else:
            left = mid + 1
    answer = left
    return answer

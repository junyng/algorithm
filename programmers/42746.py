import heapq 

def solution(numbers):
    heap = []
    numbers = list(map(str, numbers))
    
    for number in numbers:
        heapq.heappush(heap, (number * 3, number))
    
    temp = []
    while heap:
        temp.append(str(heapq.heappop(heap)[1]))
    
    temp.reverse()
    
    return str(int(''.join(temp)))

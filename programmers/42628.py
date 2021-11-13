import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    
    for operation in operations:
        command = operation.split()
        
        if command[0] == "I":
            number = int(command[1])
            heapq.heappush(min_heap, number)
            heapq.heappush(max_heap, (-number, number))
        elif min_heap:
            if command[1] == "1":
                number = heapq.heappop(max_heap)[1]
                min_heap.remove(number)
            elif command[1] == "-1":
                number = heapq.heappop(min_heap)
                max_heap.remove((-number, number))
                
    if not min_heap:
        return [0, 0]
    
    return [heapq.heappop(max_heap)[1], heapq.heappop(min_heap)]

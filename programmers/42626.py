import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    count = 0
    
    while(len(scoville) > 1 and scoville[0] < K):
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        blended = first + second * 2
        count += 1
        heapq.heappush(scoville, blended)
    
    if scoville[0] > K:
        return count
    else:
        return -1

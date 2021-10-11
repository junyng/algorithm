import heapq

def solution(jobs):
    answer, time, index = 0, 0, 0
    start_time = -1
    heap = []
    
    jobs.sort()
    
    while (index < len(jobs)):
        for job in jobs[index:]:
            if start_time < job[0] <= time:
                heapq.heappush(heap, [job[1], job[0]])
                print(heap, index)
        if heap:
            job = heapq.heappop(heap)
            start_time = time
            time += job[0]
            answer += (time - job[1])
            index += 1
        else:
            time += 1
    return answer // len(jobs)

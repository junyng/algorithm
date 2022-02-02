def solution(priorities, location):
    works = list(enumerate(priorities))
    priorities.sort(reverse=True)
    answer = 1
    
    while(priorities):
        running_work = priorities.pop(0)
        for index, work in enumerate(works):
            if work[1] == running_work:
                if work[0] == location:
                    return answer
                works = works[index+1:] + works[:index]
                answer += 1
                break

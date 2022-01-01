from collections import deque
from collections import Counter

for _ in range(int(input())):
    n, m = map(int, input().split())
    documents = list(enumerate(list(map(int, input().split()))))
    priorities = list(map(lambda document: document[1], documents))
    counter = Counter(priorities)
    queue = deque(documents)
    count = 0
    
    while queue:
        document = queue.popleft()
        high = max(counter.keys())
        
        if document[1] < high:
            queue.append(document)
        else:
            count += 1
            counter[document[1]] -= 1
            
            if counter[document[1]] == 0:
                del counter[document[1]]
            
            if document[0] == m:
                break
    print(count)

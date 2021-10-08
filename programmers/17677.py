from collections import Counter

def solution(str1, str2):
    counter1 = Counter()
    counter2 = Counter()
    value = 65536
    
    for i in range(len(str1) - 1):
        first = str1[i]
        second = str1[i+1]
        word = (first + second).lower()
        if first.isalpha() and second.isalpha():
            if word not in counter1:
                counter1[word] = 1
                continue
            counter1[word] += 1
        
    for i in range(len(str2) - 1):
        first = str2[i]
        second = str2[i+1]
        word = (first + second).lower()
        if first.isalpha() and second.isalpha():
            if word not in counter2:
                counter2[word] = 1
                continue
            counter2[word] += 1
        
    intersection = list((counter1 & counter2).elements())
    union = list((counter1 | counter2).elements())
    
    if len(union) == 0 and len(intersection) == 0: return value
    
    return int(len(intersection) / len(union) * value)

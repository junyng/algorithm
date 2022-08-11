from collections import Counter

while True:
    string = input()
    
    if string == "*": break

    for D in range(len(string)):
        start = 0
        end = start + D + 1
        
        counter = Counter()
        
        while end < len(string):
            sub_string = string[start] + string[end]
            counter[sub_string] += 1
            
            start += 1
            end = start + D + 1
        
        if len(counter.keys()) < sum(counter.values()):
            print('{} is NOT surprising.'.format(string))
            break
        
        if D == len(string) - 1:
            print('{} is surprising.'.format(string))

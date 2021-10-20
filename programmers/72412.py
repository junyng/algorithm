from itertools import product
from bisect import bisect_left

def solution(infos, queries):
    languages = ['cpp', 'java', 'python']
    positions = ['backend', 'frontend']
    careers = ['junior', 'senior']
    soulfoods = ['chicken', 'pizza']
    
    apply_list = dict()
    
    for info in infos:
        items = info.split(' ')
        l = items[0] in languages and [items[0], '-'] or languages + ['-']
        p = items[1] in positions and [items[1], '-'] or positions + ['-']
        c = items[2] in careers and [items[2], '-'] or careers + ['-']
        s = items[3] in soulfoods and [items[3], '-'] or soulfoods + ['-']
        keys = list(product(l, p, c, s))
        
        for key in keys:
            if key in apply_list:
                apply_list[key].append(int(items[4]))
            else:
                apply_list[key] = [int(items[4])]
    answer = []
    
    for key in apply_list.keys():
        apply_list[key].sort()
    
    for query in queries:
        items = list(filter(lambda item: item != 'and', query.split(' ')))
        key = tuple(items[:-1])
        if key in apply_list:
            scores = apply_list[key]
            count = len(scores) - bisect_left(scores, int(items[4]))
            answer.append(count)
        else:
            answer.append(0)
    return answer

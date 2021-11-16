from itertools import combinations

def is_subset(keys, group): 
    for key in keys:
        key, group = set(key) , set(group)
        if key.issubset(group):
            return True
    else:
        return False

def solution(relation):
    candidate_keys = []
    count = 0
    for index in range(1, len(relation)+1):
        relation_groups = list(combinations(range(len(relation[0])), index))
        for relation_group in relation_groups:
            if is_subset(candidate_keys, relation_group):
                continue
            tuples = set()
            for i in range(len(relation)):
                key = "".join([relation[i][v] for v in relation_group])
                tuples.add(key)
            if len(tuples) == len(relation):
                count += 1
                candidate_keys.append(relation_group)
    return len(candidate_keys)

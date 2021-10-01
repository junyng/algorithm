from operator import itemgetter

def solution(food_times, k):
    foods = []
    n = len(food_times)
    for i in range(n):
        foods.append((food_times[i], i+1))
        
    foods.sort()
    
    time = 0
    
    for i, food in enumerate(foods):
        diff = food[0] - time
        if diff != 0:
            spend = diff * n
            if spend <= k:
                k -= spend
                time = food[0]
            else:
                k %= n
                leftovers = sorted(foods[i:], key = itemgetter(1))
                return leftovers[k][1]
        n -= 1
    
       
    return -1

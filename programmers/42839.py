from itertools import permutations

def is_prime_number(x):
    if x < 2: return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    numbers = list(map(str, numbers))
    arr = set()
    for i in range(1, len(numbers) + 1):
        per = list(map(''.join, permutations(numbers, i)))
        for p in per:
            arr.add(int(p))
    
    answer = 0
    for number in arr:
        if is_prime_number(number):
            answer += 1
    
    return answer

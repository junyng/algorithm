import sys
import math

N, M = map(int, sys.stdin.readline().split())

mul = N * M

answer = 100000000

first = 0
second = 0

number = N
while (number * number <= mul):
    target = mul // number
    if math.gcd(number, target) == N and math.lcm(number, target) == M:
        if answer > number + target:
            first = number
            second = target
    number += 1

print(first, second)

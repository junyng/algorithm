import sys

N, T = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

partial_sum = [0]

for i in range(N):
    partial_sum.append(partial_sum[i] + numbers[i])

for i in range(T):
    L, R = map(int, sys.stdin.readline().split())
    print(partial_sum[R] - partial_sum[L-1])

import sys
from bisect import bisect_right

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

for index, ink in enumerate(A):
    print(bisect_right(B, ink) - index - 1, end=' ')

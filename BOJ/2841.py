#pypy3
import sys

n, p = map(int, sys.stdin.readline().split())
lines = [[] for i in range(7)]
count = 0

for _ in range(n):
    number, fret = map(int, sys.stdin.readline().split())

    while True:
        line = lines[number]
        
        if not line:
            line.append(fret)
            count += 1
            break
        elif line[-1] == fret:
            break
        elif line[-1] < fret:
            line.append(fret)
            count += 1
            break
        else:
            line.pop()
            count += 1

print(count)

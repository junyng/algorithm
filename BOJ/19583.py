import sys
from collections import defaultdict

start, end, streaming_end = sys.stdin.readline().split()

start = int(start[:2]) * 60 + int(start[3:])
end = int(end[:2]) * 60 + int(end[3:])
streaming_end = int(streaming_end[:2]) * 60 + int(streaming_end[3:])

counter = defaultdict(int)

for line in sys.stdin.readlines():
    time, name = line.split()
    time = int(time[:2]) * 60 + int(time[3:])
    
    if time <= start:
        counter[name] = 1
    elif end <= time <= streaming_end and counter[name] == 1:
        counter[name] = 2

count = 0

for value in counter.values():
    if value == 2:
        count += 1

print(count)

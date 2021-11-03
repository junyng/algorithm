person = list(map(int, input().split()))
person.sort()

group = 0
count = 0
for p in person:
    count += 1
    if p == count:
        group += 1
        count = 0

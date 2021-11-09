score = list(input())
score = list(map(lambda x: int(x), score))
mid = len(score) // 2
first = score[:mid]
second = score[mid:]

if sum(first) == sum(second):
    print("LUCKY")
else:
    print("READY")

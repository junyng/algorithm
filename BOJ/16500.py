s = input()
n = int(input())
words = ['' for _ in range(1000)]
dp = [0 for _ in range(1000)]
dp[len(s)] = 1

for i in range(n):
    words[i] = input()

for i in range(len(s)-1, -1, -1):
    for j in range(n+1):
        if s.find(words[j], i) == i and dp[i + len(words[j])] == 1:
            dp[i] = 1
            break
        else:
            dp[i] = 0

print(dp[0])

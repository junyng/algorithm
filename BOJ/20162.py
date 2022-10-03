N = int(input())

dp = [0] * (N+1)
snacks = [0] * (N+1)

for i in range(1, N+1):
    snacks[i] = int(input())

dp[1] = snacks[1]
result = dp[1]

for i in range(2, N+1):
    dp[i] = snacks[i]
    for j in range(1, i):
        if snacks[j] < snacks[i]:
            dp[i] = max(dp[i], dp[j] + snacks[i])
    
    result = max(result, dp[i])

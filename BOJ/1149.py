n = int(input())
dp = [[0] * 3 for _ in range(1001)]
costs = [[]]

for i in range(n):
    costs.append(list(map(int, input().split())))

for i in range(1, n+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

print(min(dp[n][0], dp[n][1], dp[n][2]))

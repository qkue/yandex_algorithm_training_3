# Python 3.12.1

n, k = map(int, input().split())

dp = [0] * (n + k)
dp[0] = 1

for i in range(1, k + 1):
    for j in range(0, i):
        dp[i] += dp[j]

for i in range(k + 1, n + 1):
    for j in range(i - k, i):
        dp[i] += dp[j]

print(dp[n - 1])

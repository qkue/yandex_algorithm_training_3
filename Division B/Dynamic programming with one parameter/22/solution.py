# Python 3.12.1
# Разбор задания с получением формул https://site.ada.edu.az/~medv/acm/Docs%20e-olimp/Volume%2041/4051.htm

n, k = map(int, input().split())

dp = [0] * (30 + 1)
dp[1] = 1
dp[2] = 1

for i in range(3, k + 1):
    dp[i] = 2 * dp[i - 1]
for i in range(k + 1, n + 1):
    if i > 2:
        dp[i] = 2 * dp[i - 1] - dp[i - k - 1]

print(dp[n])



# наивная реализация
"""
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
"""

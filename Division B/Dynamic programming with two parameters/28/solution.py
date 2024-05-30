# Python 3.12.1
# Подробный разбор решения https://site.ada.edu.az/~medv/acm/Docs%20e-olimp/Volume%2041/4021.htm

n, m = map(int, input().split())
dp = []
inf = 0
dp.append([inf] * (m + 1))

for _ in range(n):
    row = [0] * (m + 1)
    dp.append(row)
dp[1][1] = 1

for row in range(2, n + 1):
    for col in range(2, m + 1):
        dp[row][col] = dp[row - 2][col - 1] + dp[row - 1][col - 2]

print(dp[n][m])

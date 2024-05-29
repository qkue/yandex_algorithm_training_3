# Python 3.12.1
# Разбор с комментариями https://site.ada.edu.az/~medv/acm/Docs%20e-olimp/Volume%2010/987.htm

n = int(input())
arr = [0] + sorted(list(map(int, input().split())))
dp = [0] * (101)
dp[2] = arr[2] - arr[1]
if n > 2:
    dp[3] = arr[3] - arr[1]

for i in range(4, n + 1):
    dp[i] = min(dp[i - 1], dp[i - 2]) + arr[i] - arr[i - 1]

print(dp[n])

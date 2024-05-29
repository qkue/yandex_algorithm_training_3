# Python 3.12.1
# Хороший разбор задания https://site.ada.edu.az/~medv/acm/Docs%20e-olimp/Volume%203/263.htm 

n = int(input())

num = [2, 4, 7]
for i in range(3, n):
    num.append(num[i - 1] + num[i - 2] + num[i - 3])
print(num[n - 1])

"""
# Рекурсия с мемоизацией

n = int(input())

dp = [-1] * (n + 3)
dp[1] = 2
dp[2] = 4
dp[3] = 7

def func(n):
    if dp[n] != -1: 
        return dp[n]
    
    dp[n] = (func(n - 1) + func(n - 2) + func(n - 3))
    return dp[n]

print(func(n))
"""

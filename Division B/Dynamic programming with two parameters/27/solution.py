# Python 3.12.1

n, m = map(int, input().split())
arr = []
dp = []
inf = 0

arr.append([inf] * (m + 1))
dp.append([inf] * (m + 1))
for _ in range(n):
    row = list(map(int, input().split()))
    arr.append([inf] + row)
    dp.append([inf] + row)

dp_i = [-1, 0]
dp_j = [0, -1]

for row in range(1, n + 1):
    for col in range(1, m + 1):
        turn = inf
        for ind in range(len(dp_i)):
            value = arr[row + dp_i[ind]][col + dp_j[ind]]
            if turn < value:
                turn = value
        arr[row][col] += turn

print(arr[-1][-1])


# reverse
backtrack = []
last_i = n
last_j = m
while not (last_i == 1 and last_j == 1):
    current_num = arr[last_i][last_j]
    default_num = dp[last_i][last_j]
    search_num = current_num - default_num
    for ind in range(len(dp_i)):
        value = arr[last_i + dp_i[ind]][last_j + dp_j[ind]]
        if value == search_num:
            last_i = last_i + dp_i[ind]
            last_j = last_j + dp_j[ind]
            if dp_i[ind] == -1:
                backtrack.append('D')
            else:
                backtrack.append('R')
            break

for char in range(len(backtrack)-1, -1, -1):
    print(backtrack[char], end=' ')

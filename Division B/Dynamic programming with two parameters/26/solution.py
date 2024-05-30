# Python 3.12.1

n, m = map(int, input().split())
arr = []
dp = []
inf = 10**6

arr.append([inf] * (m + 1))

for _ in range(n):
    row = list(map(int, input().split()))
    arr.append([inf] + row)
arr[0][0], arr[1][0] = 0, 0

dp_i = [-1, 0]
dp_j = [0, -1]

for row in range(1, n + 1):
    for col in range(1, m + 1):
        turn = inf
        for ind in range(len(dp_i)):
            value = arr[row + dp_i[ind]][col + dp_j[ind]]
            if turn > value:
                turn = value
        arr[row][col] += turn
#print(arr)
print(arr[-1][-1])

# Python 3.12.1

n = int(input())
arr_n = list(map(int, input().split()))
m = int(input())
arr_m = list(map(int, input().split()))
 
table = [[0] * (m + 1) for _ in range(n + 1)]

# create table and fill
for row in range(1, n + 1):
    for col in range(1, m + 1):
        table[row][col] = max(table[row - 1][col], table[row][col - 1])
        if arr_n[row - 1] == arr_m[col - 1]:
            table[row][col] = max(table[row][col], table[row - 1][col - 1] + 1)

# backtracking
answer = []
row = n
col = m
while row > 0 and col > 0:
    if table[row - 1][col] == table[row][col]:
        row -= 1
    elif table[row][col - 1] == table[row][col]:
        col -= 1
    else:
        answer.append(arr_n[row - 1])
        row -= 1
        col -= 1

answer = answer[::-1]
print(*answer)

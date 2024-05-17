# Python 3.9 (PyPy 7.3.11)

n, m, k = map(int, input().split())
matrix = []
prefixsum_row = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
    prefixsum_row.append([0])
    for elem in range(1, len(row) + 1):
        prefixsum_row[i].append(prefixsum_row[i][elem-1] + row[elem - 1])

answer = []
for i in range(k):
# for i in range(1):
    x1, y1, x2, y2 = map(int, input().split()) # t.split()) 
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1

    current_res = 0
    for j in range(x1 - 1, x2):
        current_res += prefixsum_row[j][y2] - prefixsum_row[j][y1 - 1]
    answer.append(str(current_res))

print('\n'.join(answer))

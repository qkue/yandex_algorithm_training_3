# Python 3.12.3

from sys import stdin

N, M, S, T, Q = map(int, stdin.readline().split())
table = [[500 if (row > 1 and row < 2 + N) and (col > 1 and col < 2 + M) else -1 
                            for col in range(M + 4)] for row in range(N + 4)]

table[S + 1][T + 1] = 0

"""
-1 = непроходимое поле, граница
0 = точка старта, кормушка
500 = точка поля, ещё не высчитывалась

"""
d_row = [-1, -2, -2, -1, 1, 2, 2, 1]
d_col = [-2, -1, 1, 2, 2, 1, -1, -2]
list_points = [[] for _ in range((N + M))]
list_points[0].append((S + 1, T + 1))

for number in range(len(list_points)):
    for coord in list_points[number]:
        row, col = coord
        
        for swift in range(len(d_row)):
            move_row = row + d_row[swift]
            move_col = col + d_col[swift]
            if table[move_row][move_col] == 500:
                table[move_row][move_col] = number + 1
                list_points[number + 1].append((move_row, move_col))

cnt_moves = 0
isPath = True

for _ in range(Q):
    x, y = map(int, stdin.readline().split())
    flea = table[x + 1][y + 1]
    if flea == 500 or flea == -1:
        isPath = False
        break
    cnt_moves += flea

if isPath:
    print(cnt_moves)
else: 
    print(-1)

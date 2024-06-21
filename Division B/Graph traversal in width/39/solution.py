# Python 3.12.3

from sys import stdin

n = int(stdin.readline().strip())
cave = []
cave.append([[-1] * (n + 2) for _ in range(n + 2)])
cave.extend([[] for _ in range(n)])
start = ()

cave.append([[-1] * (n + 2) for _ in range(n + 2)])
for level in range(1, n + 1):
    _ = stdin.readline()
    upper = [-1] * (n + 2)
    cave[level].append(upper)
    for sublevel in range(n):
        
        piece = [-1]
        text = stdin.readline().strip()
        for sym in text:
            if sym == '#':
                piece.append(-1)
            elif sym == '.':
                piece.append(-2)
            elif sym == 'S':
                piece.append(0)
                start = (level, sublevel + 1, text.find('S') + 1)
        
        piece.append(-1)
        cave[level].append(piece)
    lower = [-1] * (n + 2)
    cave[level].append(lower)

"""
# or (-1) = непроходимое поле, граница
S or (0) = точка старта, кормушка
. or (-2)= свободная клетка

"""
d_level = [1, -1, 0, 0, 0, 0]
d_sublevel = [0, 0, 0, 0, -1, 1]
d_place = [0, 0, -1, 1, 0, 0]

list_points = [[] for _ in range((n ** 3 + 1))]
list_points[0].append(start)
min_moves = n ** 4

for num in range(len(list_points)):
    for coord in list_points[num]:
        level, sublevel, place = coord

        for swift in range(len(d_level)):
            move_level = level + d_level[swift]
            move_sublevel = sublevel + d_sublevel[swift]
            move_place = place + d_place[swift]
            if cave[move_level][move_sublevel][move_place] == -2:
                cave[move_level][move_sublevel][move_place] = num + 1
                list_points[num + 1].append((move_level, move_sublevel, move_place))
                if move_level == 1 and min_moves > num + 1:
                    min_moves = num + 1
                    
print(min_moves)

# Python 3.12.3

from sys import stdin, setrecursionlimit
setrecursionlimit(250000) # обязательное условие

def dfs(graph, colors, now, answer):
    isBad = False
    colors[now] = 1
    for neig in graph.get(now, {}):
        if colors[neig] == 0:
            isBad = dfs(graph, colors, neig, answer)
        if isBad:
            return isBad
        if colors[neig] == 1:
            # print(f'neig = {neig}, now = {now}, colors = {colors}')
            isBad = True
            return isBad

    colors[now] = 2
    answer.append(now)
    return isBad

n, m = map(int, stdin.readline().split())
vertex_dict = dict()

for _ in range(m):
    left, right = map(int, stdin.readline().split())
    if left not in vertex_dict:
        vertex_dict[left] = []
    # if right not in vertex_dict:
    #     vertex_dict[right] = []
    
    vertex_dict[left].append(right)
    # vertex_dict[right].append(left)

colors = [0] * (n + 1)
"""
0 - white
1 - grey
2 - black

"""
answer = []
isBad = False
for comp in range(1, n + 1):
    if colors[comp] == 0:
        isBad = dfs(vertex_dict, colors, comp, answer)
        if isBad:
            break

if isBad:
    print(-1)
else:
    answer.reverse()
    print(*answer)


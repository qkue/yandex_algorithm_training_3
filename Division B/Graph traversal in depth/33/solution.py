# Python 3.12.3

from sys import stdin, setrecursionlimit
setrecursionlimit(30000)

n, m = map(int, stdin.readline().split())

def dfs(graph, visited, now, colors, dye):
    visited.add(now)
    colors[now] = dye
    #print(f'now = {now}, dye = {dye}')
    for neig in graph.get(now, {}):
        #print(f'now = {now}, neig = {neig}, dye neig = {colors[neig]}')
        if colors[neig] == dye:
            #print('f')
            global isSeparate
            isSeparate = True
        if neig not in visited:
            dfs(graph, visited, neig, colors, 3 - dye)

vertex_dict = dict()


for _ in range(m):
    left, right = map(int, stdin.readline().split())
    if left not in vertex_dict:
        vertex_dict[left] = []
    if right not in vertex_dict:
        vertex_dict[right] = []
    
    vertex_dict[left].append(right)
    vertex_dict[right].append(left)

all_visit = set()
isSeparate = False
colors = [0] * (n + 1)

for comp in range(1, n + 1):
    if comp not in all_visit:
        visit = set()
        dye = 1
        dfs(vertex_dict, visit, comp, colors, dye)
        all_visit.update(visit)
        if isSeparate:
            break

#print(colors)
#print(isSeparate)
if isSeparate:
    print("NO")
else:
    print("YES")


# Python 3.12.3

from sys import stdin, setrecursionlimit
setrecursionlimit(10000)

n, m = map(int, stdin.readline().split())

def dfs(graph, visited, now):
    visited.add(now)
    for neig in graph.get(now, {}):
        if neig not in visited:
            dfs(graph, visited, neig)

vertex_dict = dict()
k = 1
visit = set()


for _ in range(m):
    left, right = map(int, stdin.readline().split())
    if left not in vertex_dict:
        vertex_dict[left] = []
    if right not in vertex_dict:
        vertex_dict[right] = []

    vertex_dict[left].append(right)
    vertex_dict[right].append(left)

dfs(vertex_dict, visit, 1)

print(len(visit))
print(*sorted(visit))

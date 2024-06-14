# Python 3.12.3

from sys import stdin, setrecursionlimit
setrecursionlimit(30000)

n, m = map(int, stdin.readline().split())

def dfs(graph, visited, now):
    visited.add(now)
    for neig in graph.get(now, {}):
        if neig not in visited:
            dfs(graph, visited, neig)

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
comp_cnt = 0
answer = []

for comp in range(1, n + 1):
    if comp not in all_visit:
        visit = set()
        dfs(vertex_dict, visit, comp)
        answer.append(len(visit))
        answer.append(' '.join(map(str, sorted(visit))))
        all_visit.update(visit)
        comp_cnt += 1

print(comp_cnt)
print("\n".join(map(str, answer)))

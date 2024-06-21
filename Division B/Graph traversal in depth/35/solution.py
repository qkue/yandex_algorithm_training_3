# Python 3.12.3

from sys import stdin, setrecursionlimit
setrecursionlimit(250000)


def dfs(graph, colors, now, answer, visited):
    isCycle = 3
    """
    3 - цикл не найден
    4 - цикл найден
    5 - строится цикл (это состояние только внутри функции dfs)
    
    """
    colors[now] = 1
    for neig in graph.get(now, []):
        if colors[neig] == 0:
            visited.add((now, neig))
            isCycle = dfs(graph, colors, neig, answer, visited)
        
        if isCycle == 4:
            return isCycle
        elif isCycle == 5:
            if now == colors[-1]:
                isCycle = 4
            #elif now != colors[-1]:
            answer.append(now)
            return isCycle

        if colors[neig] == 1 and ((neig, now) not in visited):
            #print(f'neig = {neig}, now = {now}, colors = {colors}')
            isCycle = 5
            answer.append(now)
            colors.append(neig)
            return isCycle

    colors[now] = 2
    #answer.append(now)
    return isCycle

n = int(stdin.readline().strip())
vertex_dict = dict()

for num in range(1, n + 1):
    numbers = list(map(int, stdin.readline().split()))
    if num not in vertex_dict:
        vertex_dict[num] = []

    for edge in range(len(numbers)):
        if numbers[edge]:
            vertex_dict[num].append(edge + 1)

#print(vertex_dict)
colors = [0] * (n + 1)
"""
0 - white
1 - grey
2 - black

"""
visited = set()
answer = []
#isCycle = False
for comp in range(1, n + 1):
    if colors[comp] == 0:
        isCycle = dfs(vertex_dict, colors, comp, answer, visited)
        """
        3 - цикл не найден
        4 - цикл найден
        5 - строится цикл (это состояние только внутри функции dfs)
        
        """
        if isCycle == 4:
            break

if isCycle == 3:
    print("NO")
else:
    colors.pop()
    #answer.reverse()
    print("YES")
    print(len(answer))
    print(*answer)


# Python 3.12.3

from sys import stdin

class Queue:
    def __init__(self, cnt):
        self.cnt = cnt
        self.array = [0] * self.cnt
        self.begin = 0
        self.last = 0

    def pop_left(self):
        item = self.array[self.begin]
        self.begin = (self.begin + 1) % self.cnt
        return item
    
    def push_back(self, item):
        self.array[self.last] = item
        self.last = (self.last + 1) % self.cnt
    
    def length(self):
        return abs(self.last - self.begin)


n = int(stdin.readline().strip())
vertex = dict()

for row in range(1, n + 1):
    nums = list(map(int, stdin.readline().split()))
    if row not in vertex:
            vertex[row] = []
        
    for col in range(n):
        if nums[col]:
            vertex[row].append(col + 1)

#print(vertex)
#visited = set()
list_vertexes = [1000] * (n + 1)
started, finished = map(int, stdin.readline().split())
list_vertexes[started] = 0

que = Queue(n)
que.push_back(started)

while que.length():
    
    now = que.pop_left()
    #print(f'now = {now}')
    for point in vertex.get(now, []):
        #print(f'now = {now}, point = {point}')
        if list_vertexes[point] == 1000:
            que.push_back(point)
            list_vertexes[point] = min(list_vertexes[point], list_vertexes[now] + 1)

if list_vertexes[finished] == 1000:
    print(-1)
else:
    print(list_vertexes[finished])

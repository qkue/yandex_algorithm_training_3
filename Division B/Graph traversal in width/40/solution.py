# Python 3.12.3

from sys import stdin

answer = -1
n = int(stdin.readline().strip())
m = int(stdin.readline().strip())
metro = [[]] * m
for i in range(m):
    nums = set(list(map(int, stdin.readline().split()))[1::])
    metro[i] = nums

departure, arrive = map(int, stdin.readline().split())
#print(metro)
vertex_departure = [i for i in range(len(metro)) if departure in metro[i]]
vertex_arrive = {i for i in range(len(metro)) if arrive in metro[i]}

list_points = [[] for _ in range((m * 2))]
list_points[0] = vertex_departure
list_destination = [100 * 2] * m
for i in vertex_departure:
    list_destination[i] = 0
visited = set()
#print(list_points)

for num in range(len(list_points)):

    #print(list_points)
    for number in list_points[num]:
        visited.add(number)

        for line in range(len(metro)):
            if line not in visited and (metro[line].intersection(metro[number])):
                list_points[num + 1].append(line)
                list_destination[line] = min(list_destination[line], num + 1)

answer = 200
for i in vertex_arrive:
    if answer > list_destination[i]:
        answer = list_destination[i]

if answer == 200:
    print(-1)
else:
    print(answer)

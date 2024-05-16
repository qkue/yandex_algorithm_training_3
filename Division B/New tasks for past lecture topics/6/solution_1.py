# Python 3.12.1
# Это простой алгоритм, который перебирает события и если позже в эти сектора была установка, событие отбрасывается.

m = int(input())
n = int(input())
events = []

for i in  range(1, n + 1):
    a, b = map(int, input().split())
    events.append((a, b))

answer = 0

for event in range(len(events)):
    flag = True
    a, b = events[event]
    for seg in range(event + 1, len(events)):
        c, d = events[seg]
        if a <= d and c <= b:
            flag = False
            break
    if flag:
        answer += 1
print(answer)

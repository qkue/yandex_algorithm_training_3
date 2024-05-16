# Python 3.12.1
# По условию задачи здесь кажется, что подходит сканирующая прямая, но её отлаживание на соответствие условию "...если очередной раздел хотя бы по одному сектору пересекается с каким-то ранее созданным разделом, то ранее созданный раздел «затирается»..." заняло несколько часов. Потому что в начальной реализации, у меня получилось, что если попадается последняя по времени установка производилась на начальные сектора и была беспрерывная цепочка событий дальше, они затирались все. Вот такая бага.

m = int(input())
n = int(input())
events = []

for i in  range(1, n + 1):
    a, b = map(int, input().split())
    events.append((a, -1, i))
    events.append((b, 1, i))
events.sort()

answer = 0
deleted = set()
current = 0
oper_system = set()
oper_system.add(0)

for event in events:
    if event[1] == -1:
        oper_system.add(event[2])
        if event[2] > current:
            if current:
                deleted.add(current)
            current = event[2]    
        elif event[2] < current:
            deleted.add(event[2])
    

    elif event[1] == 1:
        oper_system.remove(event[2])
        if event[2] not in deleted:
            answer += 1
        if event[2] == current:
            current = max(oper_system)

print(answer)

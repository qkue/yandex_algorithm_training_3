# Python 3.12.1
# Алгоритм аналогичный лекции и содержит тот же "грязный хак" на последний элемент, снижающий количество требуемых проверок

def push_heap(heap, item):
    heap.append(item)
    pos = len(heap) - 1
    while pos > 0 and heap[pos] > heap[(pos - 1) // 2]:
        heap[(pos - 1) // 2], heap[pos] = heap[pos], heap[(pos - 1) // 2]
        pos = (pos - 1) // 2

def pop_heap(heap):
    ans = heap[0]
    heap[0] = heap[-1]
    pos = 0
    while pos * 2 + 2 < len(heap):
        man_son = pos * 2 + 1
        if heap[pos * 2 + 2] > heap[man_son]:
            man_son = pos * 2 + 2
        
        if heap[pos] < heap[man_son]:
            heap[pos], heap[man_son] = heap[man_son], heap[pos]
            pos = man_son
        else:
            break
    heap.pop()
    return ans

answer = []
heap_list = []
n = int(input())
for _ in range(n):
    cmd = list(map( int, input().split()))
    if cmd[0] == 0:
        push_heap(heap_list, cmd[1])
    elif cmd[0] == 1:
        answer.append(pop_heap(heap_list))

print('\n'.join(str(elem) for elem in answer))

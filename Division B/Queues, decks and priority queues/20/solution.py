# Python 3.12.1

def sifting(heap, pos):
    while pos * 2 + 1 < len(heap):
        max_son = pos * 2 + 1
        if (pos * 2 + 2) < len(heap) and heap[pos * 2 + 2] > heap[max_son]:
            max_son = pos * 2 + 2
        
        if heap[pos] < heap[max_son]:
            heap[pos], heap[max_son] = heap[max_son], heap[pos]
            pos = max_son
        else:
            break
        
def pop_heap(heap, len_heap):
    ans = heap[0]
    heap[0] = heap[len_heap - 1]
    pos = 0
    while pos * 2 + 2 < len_heap:
        man_son = pos * 2 + 1
        if heap[pos * 2 + 2] > heap[man_son]:
            man_son = pos * 2 + 2
        
        if heap[pos] < heap[man_son]:
            heap[pos], heap[man_son] = heap[man_son], heap[pos]
            pos = man_son
        else:
            break
    return ans

n = int(input())
heap_list = list(map(int, input().split()))

mid = n // 2 - 1
for num in range(mid, -1, -1):
    sifting(heap_list, num)

for num in range(n, 0, -1):
    last = pop_heap(heap_list, num)
    heap_list[num - 1] = last

print(*heap_list)

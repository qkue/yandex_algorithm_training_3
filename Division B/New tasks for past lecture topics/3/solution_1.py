# Python 3.12.1	

n = input()

diego_num = (sorted(set(map(int, input().split()))))
k = int(input())
collectioneers = list(map(int, input().split()))
answer = []
n = len(diego_num)

for collectioner in collectioneers:
    left = 0
    right = n
    if collectioner < diego_num[left]:
        #answer.append(0)
        pass
    elif collectioner > diego_num[right - 1]:
        left = n
    else:    
        while left < right:
            m = (left + right) // 2
            if diego_num[m] >= collectioner:
                right = m
            else:
                left = m + 1
    answer.append(left)

print('\n'.join(str(a) for a in answer))

# Python 3.12.1

n = int(input())
diego_num = [0]
diego_num.extend(sorted(set(map(int, input().split()))))
k = int(input())
collectioneers = list(map(int, input().split()))
answer = []
n = len(diego_num) - 1

for collectioner in collectioneers:
    left = 0
    right = n
    
    while left < right:
        m = (left + right + 1) // 2
        #print(m)
        #print(diego_num)
        if diego_num[m] < collectioner:
            left = m
        else:
            right = m - 1
    answer.append(left)

print('\n'.join(str(a) for a in answer))

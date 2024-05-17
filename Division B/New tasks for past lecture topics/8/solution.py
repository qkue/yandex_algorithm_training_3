# Python 3.12.1

k = int(input())
x = []
y = []

for _ in range(k):
    left, right = map(int, input().split())
    x.append(left)
    y.append(right)

print(min(x), min(y), max(x), max(y))

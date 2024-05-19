# Python 3.12.1

class Stack:
    def __init__(self):
        self.array = []

    def push(self, item):
        self.array.append(item)

    def pop(self):
        return self.array.pop()

    def size(self):
        return True if self.array else False
    
    def back(self):
        return self.array[-1]
        

arr = Stack()
n = int(input())
cities = list(map(int, input().split()))
answer = [0] * n

for city in range(len(cities)):

    while arr.size() and arr.back()[0] > cities[city]:
        town, num = arr.pop()
        answer[num] = city

    arr.push((cities[city], city)) # city, number

while arr.size():
    town, num = arr.pop()
    answer[num] = -1

print(*answer)

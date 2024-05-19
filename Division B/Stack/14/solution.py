# Python 3.12.1

class Stack:
    def __init__(self):
        self.array = []

    def push(self, item):
        self.array.append(item)

    def pop(self):
        if not self.size():
            return None
        self.array.pop()

    def size(self):
        return True if self.array else False
    
    def back(self):
        return self.array[-1]
        

arr = Stack()
n = int(input())
trains = list(map(int, input().split()))
error = False
train_number = 0

for train in trains:
    arr.push(train)
    while arr.size() and arr.back() == train_number + 1:
        arr.pop()
        train_number += 1
if arr.size():
    print('NO')
else:
    print('YES')

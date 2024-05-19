# Python 3.12.1

class Stack:
    def __init__(self):
        self.array = []

    def push(self, command):
        self.array.append(int(command))
        print('ok')

    def pop(self):
        if self.array:
            last = self.array.pop()
            print(last)
        else:
            print('error')
    
    def back(self):
        if self.array:
            print(self.array[-1])
        else:
            print('error')

    def size(self):
        print(len(self.array))

    def clear(self):
        self.array.clear()
        print('ok')
    
arr = Stack()


inp = input().split()
while inp[0] != 'exit':
    if inp[0] == 'push':
       arr.push(inp[1])
    elif inp[0] == 'pop':
        arr.pop()
    elif inp[0] == 'back':
        arr.back()
    elif inp[0] == 'size':
        arr.size()
    elif inp[0] == 'clear':
        arr.clear()
    inp = input().split()

print('bye')

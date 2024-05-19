# Python 3.12.1

class Stack:
    def __init__(self):
        self.array = []

    def push(self, item):
        self.array.append(item)

    def pop(self, item):
        if not self.size():
            return False

        if (self.back() == '(' and item == ')') or (self.back() == '[' and item == ']') or (self.back() == '{' and item == '}'):
            last = self.array.pop()
            return True
        else:
            return False

    def size(self):
        return True if self.array else False
    
    def back(self):
        return self.array[-1]
        

arr = Stack()
text = input()
progress = True

for char in text:
    if char in ('([{'):
        arr.push(char)
    elif char in (')]}'):
        progress = arr.pop(char)
    if not progress:
        break

if progress and not arr.size():
    print('yes')
else:
    print('no')

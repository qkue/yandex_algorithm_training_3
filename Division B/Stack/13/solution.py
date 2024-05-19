# Python 3.12.1

class Stack:
    def __init__(self):
        self.array = []

    def push(self, item):
        self.array.append(item)

    def pop(self):
        if not self.size():
            return None
        return self.array.pop()

    def size(self):
        return True if self.array else False
    
    def back(self):
        return self.array[-1]
        

arr = Stack()
t = '8 7 +'
text = input().split() #t.split()
error = False

def sign_oper(sign, left, right):
    res = 0
    if sign == '-':
        res = left - right
    elif sign == '+':
        res = left + right
    elif sign == '*':
        res = left * right
    return res

for char in text:
    if char in '+-*':
        right = arr.pop()
        left = arr.pop()
        if right == None or left == None:
            error = True
            break
        result = sign_oper(char, left, right)
        arr.push(result)

    else:
        arr.push(int(char))

print(arr.back())

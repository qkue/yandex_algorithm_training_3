# Python 3.12.1
# Реализация на круговом буфере, думал будут тяжелые тесты... Спойлеры: их не будет :)

class Dequeue:

    def __init__(self):
        self.container = [0] * 100
        self.front = 0
        self.back = 0
        self.n = 100
        self.length = 0

    def push_front(self, item):
        self.front = (self.front - 1) % self.n
        # self.front -= 1
        self.container[self.front] = item
        self.length += 1
        

    def push_back(self, item):
        # self.back += 1
        self.container[self.back] = item
        self.back = (self.back + 1) % self.n
        self.length += 1

    def pop_front(self):
        if self.size():
            item = self.container[self.front]
            # self.front += 1
            self.front = (self.front + 1) % self.n
            self.length -= 1
            return item

        else:
            return 'error'
        
    def pop_back(self):
        if self.size():
            self.back = (self.back - 1 + self.n) % self.n
            item = self.container[self.back]
            # self.back -= 1
            self.length -= 1
            return item
        else:
            return 'error'

    def front_elem(self):
        if self.size():
            item = self.container[self.front]
            return item
        else:
            return 'error'
    
    def back_elem(self):
        if self.size():
            item = self.container[(self.back - 1 + self.n) % self.n]
            return item
        else:
            return 'error'
    
    def clear_elem(self):
        self.container = [0] * 200
        self.front = 99
        self.back = 99
        self.length = 0

    def size(self):
        return (self.length) 

answer = []
deq = Dequeue()
while True:
    command = input().split()
    if command[0] == 'push_back':
        deq.push_back(command[1])
        answer.append('ok')
    elif command[0] == 'push_front':
        deq.push_front(command[1])
        answer.append('ok')
    elif command[0] == 'pop_back':
        item = deq.pop_back()
        answer.append(item)
    elif command[0] == 'pop_front':
        item = deq.pop_front()
        answer.append(item)
    elif command[0] == 'front':
        item = deq.front_elem()
        answer.append(item)
    elif command[0] == 'back':
        item = deq.back_elem()
        answer.append(item)
    elif command[0] == 'size':
        item = deq.size()
        answer.append(item)
    elif command[0] == 'clear':
        deq.clear_elem()
        answer.append('ok')
    elif command[0] == 'exit':
        answer.append('bye')
        break

print('\n'.join(str(el) for el in answer))

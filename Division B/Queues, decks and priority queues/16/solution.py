# Python 3.12.1

class Queue:

    def __init__(self):
        self.length = 0
        self.array = []
        self.front = 0

    def push_back(self, item):
        self.array.append(item)
        self.length += 1
        return 'ok'
    
    def pop_front(self):
        if self.length:
            item = self.array[self.front]
            self.front += 1
            self.length -= 1
            return item
        else:
            return 'error'
    
    def queue_front(self):
        if self.length:
            return self.array[self.front]
        else:
            return 'error'
    
    def size(self):
        return self.length

    def queue_clear(self):
        self.array.clear()
        self.length = 0
        self.front = 0
        return 'ok'

    def exit(self):
        return 'bye'

mini_queue = Queue()
res = []
while True:
    cmd = input().split()
    if cmd[0] == 'push':
        res.append(mini_queue.push_back(int(cmd[1])))
    elif cmd[0] == 'pop':
        res.append(mini_queue.pop_front())
    elif cmd[0] == 'front':
        res.append(mini_queue.queue_front())
    elif cmd[0] == 'size':
        res.append(mini_queue.size())
    elif cmd[0] == 'clear':
        res.append(mini_queue.queue_clear())
    elif cmd[0] == 'exit':
        res.append(mini_queue.exit())
        break

print('\n'.join(str(elem) for elem in res))

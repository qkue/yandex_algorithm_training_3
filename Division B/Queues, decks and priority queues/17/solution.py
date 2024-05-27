# Python 3.12.1

class Queue:

    def __init__(self):
        self.length = 0
        self.array = []
        self.front = 0
        self.back = 0
        self.circle_size = 0

    def max_size(self, item):
        self.circle_size = item
        self.array = [0] * item

    def push_back(self, item):
        ind = self.back % self.circle_size
        self.array[ind] = item
        self.back += 1
        self.length += 1
    
    def pop_front(self):
        ind = self.front % self.circle_size
        item = self.array[ind]
        self.front += 1
        self.length -= 1
        return item
    
    def size(self):
        return self.length

    def __repr__(self):
        return ' '.join(str(elem) for elem in self.array)

first_player = Queue()
second_player = Queue()
first_player.max_size(10)
second_player.max_size(10)
turns = 10 ** 6
p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))

for num in range(5):
    first_player.push_back(p1[num])
    second_player.push_back((p2[num]))

while turns and first_player.size() and second_player.size():
    turns -= 1
    card_first_player = first_player.pop_front()
    card_second_player = second_player.pop_front()
    if ((card_first_player > card_second_player or (card_first_player == 0 and card_second_player == 9)) and not (card_first_player == 9 and card_second_player == 0)): # or ()):
        first_player.push_back(card_first_player)
        first_player.push_back(card_second_player)
    else:
        second_player.push_back(card_first_player)
        second_player.push_back(card_second_player)
    
if not first_player.size():
    print('second', 10 ** 6 - turns)
elif not second_player.size():
    print('first', 10 ** 6 - turns)
else:
    print('botva')

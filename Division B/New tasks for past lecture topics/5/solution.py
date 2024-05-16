#Python 3.12.1

import string

alphabet = string.ascii_lowercase
letters = dict()

n = int(input())
for i in range(n):
    letters[alphabet[i]] = int(input())
alphabet = alphabet[:n]
answer = 0

for char in range(n - 1):
    current_letter = letters[alphabet[char]]
    next_letter = letters[alphabet[char + 1]]
    if current_letter and next_letter:
        if next_letter > current_letter:
            answer += current_letter
        elif next_letter <= current_letter:
            answer += next_letter

print(answer)

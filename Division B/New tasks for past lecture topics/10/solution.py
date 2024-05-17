# Python 3.12.1

text = input()
char_dict = dict()
n = len(text)

for i in range(n):
    letter = text[i]
    char_dict[letter] = char_dict.get(letter, 0) + (i + 1) * (n - i)

for i in sorted(char_dict):
    print(f'{i}: {char_dict[i]}')

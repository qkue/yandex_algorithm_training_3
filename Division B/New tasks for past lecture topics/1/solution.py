# Python 3.12.1	

with open('input.txt', 'rt', encoding = 'utf-8') as file_input:
    text = file_input.read().rstrip()

sym_dict = {}
for sym in text:
    if sym != ' ' and sym != '\n':
        sym_dict[sym] = sym_dict.get(sym, 0) + 1
sorted_sym = sorted(sym_dict)
max_sym_cnt = max(sym_dict.values())

for row in range(max_sym_cnt, 0, -1):
    for sym in sorted_sym:
        if sym_dict[sym] >= row:
            print('#', end = '')
        else:
            print(' ', end = '')
    print()
print(''.join(sorted_sym))

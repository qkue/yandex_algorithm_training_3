# Python 3.9 (PyPy 7.3.11)

n = int(input())
text = input()
alphabet = 'qazwsxedcrfvtgbyhnujmikolp'

answer = 0

for letter in alphabet:
    right_arrow = 0
    replace = 0
    for char in range(len(text)):
        # x = text[char]
        # y = text[right_arrow]
        #if char > 0:
            
        while right_arrow < len(text):
            if text[right_arrow] == letter:
                right_arrow += 1
            elif replace < n:
                replace += 1
                right_arrow += 1
            else:
                break
        if text[char] != letter:
                replace -= 1

        if right_arrow - char > answer:
            answer = right_arrow - char

print(answer)

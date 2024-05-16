# Python 3.12.1

def check_dist(boy, n, k):
    upper_sit = boy - k # впереди
    lower_sit = boy + k # позади
    if lower_sit > n:
        return upper_sit
    elif upper_sit < 1:
        return lower_sit
    else:
        temp_upper_sit = upper_sit if upper_sit % 2 == 0 else upper_sit + 1
        temp_lower_sit = lower_sit if lower_sit % 2 == 0 else lower_sit + 1
        temp_boy_sit = boy if boy % 2 == 0 else boy + 1

        diff_table_upper = (temp_boy_sit - temp_upper_sit) // 2 - 1
        diff_table_lower = (temp_lower_sit - temp_boy_sit) // 2 - 1
        if diff_table_upper >= diff_table_lower:
            return lower_sit
        else:
            return upper_sit

n = int(input())
k = int(input())
petya_row = int(input())
petya_sit = int(input())
answer = [-1]

petya_place = petya_row * 2 - (petya_sit % 2)

if petya_place + k <= n or petya_place - k > 0:   #n - petya_place >= k:
    vasya_place = check_dist(petya_place, n, k)
    vasya_row = vasya_place // 2 + (vasya_place % 2)
    vasya_sit = 2 - vasya_place % 2
    answer = [vasya_row, vasya_sit]

print(*answer)

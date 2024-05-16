# Python 3.12.1

a = list(map(int, input().split(':')))
b = list(map(int, input().split(':')))
c = list(map(int, input().split(':')))

a_sec = ((a[0] * 60) + a[1]) * 60 + a[2]
b_sec =  ((b[0] * 60) + b[1]) * 60 + b[2]
c_sec =  ((c[0] * 60) + c[1]) * 60 + c[2]

diff_sec_a_b = (c_sec if c_sec > a_sec else (c_sec + 86400)) - a_sec
time_correspondent = (diff_sec_a_b // 2) + diff_sec_a_b % 2
b_sec += time_correspondent
if b_sec >= 86400:
    b_sec -= 86400
b_hours = b_sec // 60 // 60
b_sec -= b_hours * 60 * 60
b_minutes = b_sec // 60
b_sec -= b_minutes * 60

print(f'{b_hours:02}:{b_minutes:02}:{b_sec:02}')

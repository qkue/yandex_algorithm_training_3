# Python 3.12.1

n = int(input())
inf = 10 ** 6

coupon = 0
prices = []
for _ in range(n):
    num = int(input())
    if num > 100:
        coupon += 1
    prices.append(num)
coupon += 4

# create start table
table = [[inf] * (coupon) for _ in range(n + 1)]
table[0][1] = 0

# fill table numbers
for row in range(1, n + 1):
    diner = prices[row - 1]
    for col in range(1, coupon - 1):
        if diner <= 100:
            table[row][col] = min(table[row - 1][col] + diner, table[row - 1][col + 1])
        elif diner > 100:
            table[row][col] = min(table[row - 1][col + 1], table[row - 1][col - 1] + diner)

# find min price for coupon count
min_price_diner = inf
current_coupon = 0
for i in range(1, coupon - 1):
    price = table[-1][i]
    if min_price_diner >= price:
        min_price_diner = price
        current_coupon = i - 1

# backtracking for find days when coupon was used
days_coupon = []
current_diner = current_coupon + 1
for row in range(n, 0, -1):
    diner = prices[row - 1]
    
    if diner <= 100:
        if table[row][current_diner] - diner == table[row - 1][current_diner]:
            continue
        elif table[row][current_diner] == table[row -1][current_diner + 1]:
            days_coupon.append(row)
            current_diner += 1
    elif diner > 100:
        if table[row][current_diner] - diner == table[row - 1][current_diner - 1]:
            current_diner -= 1
        elif table[row][current_diner] == table[row - 1][current_diner + 1]:
            current_diner += 1
            days_coupon.append(row)

print(f'{min_price_diner}\n{current_coupon} {len(days_coupon)}\n{" ".join(str(num) for num in sorted(days_coupon))}')

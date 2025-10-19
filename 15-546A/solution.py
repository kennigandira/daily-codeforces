banana_cost, balance, banana_qty = map(int, input().split())

total_cost = 0
for i in range(banana_qty):
    total_cost += banana_cost * (i + 1)

if total_cost > balance:
    print(total_cost - balance)
else:
    print(0)

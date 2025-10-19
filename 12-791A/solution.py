l, b = input().split()

y = 0
while int(l) <= int(b):
    l = int(l) * 3
    b = int(b) * 2
    y += 1

print(y)


point = input()
point_left = int(point)

steps = 0
while point_left > 0:
    if point_left == 5:
        point_left -= 5
        steps += 1
    elif point_left == 4:
        point_left -= 4
        steps += 1
    elif point_left == 3:
        point_left -= 3
        steps += 1
    elif point_left == 2:
        point_left -= 2
        steps += 1
    elif point_left == 1:
        point_left -= 1
        steps += 1
    else:
        point_left -= 5
        steps += 1
print(steps)

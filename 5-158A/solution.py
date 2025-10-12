n, k = input().split(" ")

scores = input().split(" ")

total = 0

if scores[0] != '0':
    position_threshold = 0

    for index in range(len(scores)):
        # if first scores is zero or;
        # it's lesser than threshold
        if scores[index] == '0' or int(scores[index]) < position_threshold:
            break
        # if loop meets the position threshold
        # declare the position threshold
        elif index == int(k) - 1:
            position_threshold = int(scores[index])
            total += 1
        else:
            total += 1

print(total)
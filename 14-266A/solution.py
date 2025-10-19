string = input()

result = 0
for i in range(int(length) - 1):
    if string[i] == string[i + 1]:
        result += 1

print(result)

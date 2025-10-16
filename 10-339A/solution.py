numbers = input().split('+')

for l in range(len(numbers)):
    for r in range(len(numbers) - l):
        if int(numbers[l]) > int(numbers[l + r]):
            numbers[l], numbers[l + r] = numbers[l + r], numbers[l]
result = "+".join(numbers)
print(result)

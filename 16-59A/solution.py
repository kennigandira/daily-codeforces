string = input()

upper_count = 0
lower_count = 0
for char in string:
    if char.isupper():
        upper_count += 1
    else:
        lower_count += 1

if upper_count > lower_count:
    print(string.upper())
else:
    print(string.lower())

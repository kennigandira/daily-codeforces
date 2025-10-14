string = input()

distincts_char = ''

for char in string:
    if char in distincts_char:
        continue
    else:
        distincts_char += char

if len(distincts_char) == 2 or len(distincts_char) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
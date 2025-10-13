first_string = input()
second_string = input()

count = 0

for i in range(len(first_string)):
    first_char = first_string[i].lower()
    second_char = second_string[i].lower()
    if(first_char < second_char):
        count -= 1
    if(first_char > second_char):
        count += 1

print(count)
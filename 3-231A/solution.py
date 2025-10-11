n = int(input())

success = 0

for i in range(n):
    integers = input()
    count = 0
    
    splitted = integers.split(" ")
    for integer in splitted:
        if int(integer):
            count += 1
            if count == 2:
                success += 1
                break

print(success)
   



numbers = input().split(" ")

n = int(numbers[0])
k = int(numbers[1])

for i in range(k):
    if n % 10 == 0:
        n = n / 10
    else:
        n = n - 1

print(round(n))
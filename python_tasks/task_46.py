num = int(input())

for d in range(10):
    temp = num
    count = 0
    if temp == 0 and d == 0:
        count = 1
    while temp > 0:
        if temp % 10 == d:
            count += 1
        temp //= 10
    if count > 0:
        print(f"{count}", end=" ")
print()
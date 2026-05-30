num = int(input())
ans = -1

for d in range(10):
    temp = num
    count = 0
    while temp > 0:
        if temp % 10 == d:
            count += 1
        temp //= 10
    if count == 1:
        if ans == -1 or d < ans:
            ans = d

if ans == -1:
    print("нет")
else:
    print(ans)
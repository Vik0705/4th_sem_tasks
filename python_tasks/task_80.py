N = int(input())
a = list(map(int, input().split()))
count = 0
for i in range(N - 1):
    if (a[i] + a[i+1]) % 2 == 0:
        count += 1
print(count)
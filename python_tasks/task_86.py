N = int(input())
a = list(map(int, input().split()))
inv = 0
for i in range(N):
    for j in range(i + 1, N):
        if a[i] > a[j]:
            inv += 1
print(inv)
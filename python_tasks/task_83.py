N = int(input())
a = list(map(int, input().split()))
min_len = N + 1
for i in range(N):
    s = 0
    for j in range(i, N):
        s += a[j]
        if s > 0:
            min_len = min(min_len, j - i + 1)
            break 
if min_len > N:
    print("no")
else:
    print(min_len)
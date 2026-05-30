N = int(input())
a = list(map(int, input().split()))
max_len = 0
for i in range(N):
    s = 0
    for j in range(i, N):
        s += a[j]
        if s == 0:
            max_len = max(max_len, j - i + 1)
print(max_len)
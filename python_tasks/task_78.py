N = int(input())
a = list(map(int, input().split()))
max_len = 1 if N > 0 else 0
cur_len = 1
for i in range(1, N):
    if (a[i] > 0 and a[i-1] < 0) or (a[i] < 0 and a[i-1] > 0):
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 1
print(max_len)
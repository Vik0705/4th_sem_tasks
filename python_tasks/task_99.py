N = int(input())
a = list(map(int, input().split()))
max_len = 1 if N > 0 else 0
cur_len = 1
for i in range(1, N):
    if abs(a[i] - a[i-1]) == 1:
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 1
print(max_len)
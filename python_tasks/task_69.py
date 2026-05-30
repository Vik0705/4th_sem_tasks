N = int(input())
a = list(map(int, input().split()))
max_sum = a[0]
cur_sum = 0
start = 0
best_start = 0
best_end = 0
for i in range(N):
    cur_sum += a[i]
    if cur_sum > max_sum:
        max_sum = cur_sum
        best_start = start
        best_end = i
    if cur_sum < 0:
        cur_sum = 0
        start = i + 1
print(best_start, best_end)
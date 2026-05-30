N = int(input())
a = list(map(int, input().split()))
max_sum = a[0]
cur_sum = 0
for x in a:
    cur_sum += x
    if cur_sum > max_sum: max_sum = cur_sum
    if cur_sum < 0: cur_sum = 0
print(max_sum)
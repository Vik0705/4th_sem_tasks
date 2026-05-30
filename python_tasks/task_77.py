N = int(input())
a = list(map(int, input().split()))
max_len = 0
cur_len = 0
for x in a:
    if x % 2 == 0:
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 0
print(max_len)
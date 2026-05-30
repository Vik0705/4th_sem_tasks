a = list(map(int, input().split()))
max_idx = 0
for i in range(1, len(a)):
    if a[i] > a[max_idx]:
        max_idx = i
print(max_idx)
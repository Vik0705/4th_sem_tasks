N = int(input())
a = list(map(int, input().split()))
idx = -1
for i in range(1, N - 1):
    if a[i] < a[i - 1] and a[i] < a[i + 1]:
        idx = i
if idx == -1:
    print("no")
else:
    print(idx)
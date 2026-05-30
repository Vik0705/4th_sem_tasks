N = int(input())
a = list(map(int, input().split()))
count = 0
for i in range(1, N):
    if sum(a[:i]) == sum(a[i:]):
        count += 1
print(count)
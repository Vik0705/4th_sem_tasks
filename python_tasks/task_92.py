N = int(input())
M = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = []
i, j = 0, 0
while i < N and j < M:
    if a[i] < b[j]:
        res.append(a[i])
        i += 1
    else:
        res.append(b[j])
        j += 1
res.extend(a[i:])
res.extend(b[j:])
print(*res)
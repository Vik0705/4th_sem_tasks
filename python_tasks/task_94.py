a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = []
i, j = 0, 0
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        if not res or res[-1] != a[i]: res.append(a[i])
        i += 1
    elif b[j] < a[i]:
        if not res or res[-1] != b[j]: res.append(b[j])
        j += 1
    else:
        if not res or res[-1] != a[i]: res.append(a[i])
        i += 1
        j += 1
while i < len(a):
    if not res or res[-1] != a[i]: res.append(a[i])
    i += 1
while j < len(b):
    if not res or res[-1] != b[j]: res.append(b[j])
    j += 1
print(*res)
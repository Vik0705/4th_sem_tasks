a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = []
i, j = 0, 0
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        res.append(a[i])
        i += 1
    elif a[i] > b[j]:
        j += 1
    else:
        i += 1
        j += 1
res.extend(a[i:])
print(*res)
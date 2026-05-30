N = int(input())
a = list(map(int, input().split()))
found = False
for i in range(N):
    s = a[i]
    for j in range(i + 1, N):
        s += a[j]
        if s == 0:
            found = True
            break
    if found: break
print("Да" if found else "Нет")
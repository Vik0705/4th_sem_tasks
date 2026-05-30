N = int(input())
a = list(map(int, input().split()))
found = False
for i in range(N):
    for j in range(i + 1, N):
        if a[i] == a[j]:
            sub = a[i+1:j]
            if len(set(sub)) == len(sub) and a[i] not in sub:
                found = True
                break
    if found: break
print("Да" if found else "Нет")
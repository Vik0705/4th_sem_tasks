N = int(input())
a = list(map(int, input().split()))
found = False
for i in range(1, N - 1):
    for j in range(i + 1, N):
        if sum(a[:i]) == sum(a[i:j]) == sum(a[j:]):
            found = True
            break
print("Да" if found else "Нет")
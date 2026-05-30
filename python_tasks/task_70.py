N = int(input())
a = list(map(int, input().split()))
found = False
for i in range(1, N):
    if sum(a[:i]) == sum(a[i:]):
        found = True
        break
print("Да" if found else "Нет")
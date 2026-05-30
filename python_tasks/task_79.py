N = int(input())
a = list(map(int, input().split()))
found = False
s = 0
for i in range(N):
    if a[i] == s:
        found = True
        break
    s += a[i]
print("Да" if found else "Нет")
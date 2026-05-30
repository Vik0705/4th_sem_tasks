N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
found = False
for i in range(N):
    if a[-i:] + a[:-i] == b:
        found = True
        break
print("Да" if found else "Нет")
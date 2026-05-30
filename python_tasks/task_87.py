N = int(input())
a = list(map(int, input().split()))

def is_inc(lst):
    for i in range(1, len(lst)):
        if lst[i] <= lst[i-1]: return False
    return True

found = False
for i in range(N):
    for j in range(i + 1, N):
        b = a[:]
        b[i], b[j] = b[j], b[i]
        if is_inc(b):
            found = True
            break
print("Да" if found else "Нет")
N = int(input())
a = list(map(int, input().split()))

def is_inc(lst):
    for i in range(1, len(lst)):
        if lst[i] <= lst[i-1]: return False
    return True

found = False
for i in range(N):
    if is_inc(a[:i] + a[i+1:]):
        found = True
        break
print("Да" if found else "Нет")
N = int(input())
a = list(map(int, input().split()))

def is_stable(lst):
    for i in range(1, len(lst) - 1):
        if not (min(lst[i-1], lst[i+1]) <= lst[i] <= max(lst[i-1], lst[i+1])):
            return False
    return True
    
if is_stable(a):
    print("Да")
else:
    found = False
    for i in range(N):
        if is_stable(a[:i] + a[i+1:]):
            found = True
            break
    print("Да" if found else "Нет")
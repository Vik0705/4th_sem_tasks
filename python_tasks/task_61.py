N = int(input())
a = list(map(int, input().split()))

def is_pal(lst):
    return lst == lst[::-1]

possible = is_pal(a)
if not possible:
    for i in range(N):
        if is_pal(a[:i] + a[i+1:]):
            possible = True
            break
print("Да" if possible else "Нет")
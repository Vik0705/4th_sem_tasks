N = int(input())
a = list(map(int, input().split()))
max_c = max([a.count(x) for x in set(a)])
if max_c <= (N + 1) // 2:
    print("Да")
else:
    print("Нет")
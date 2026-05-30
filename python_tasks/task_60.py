N = int(input())
a = list(map(int, input().split()))
if a == a[::-1]:
    print("Да")
else:
    print("Нет")
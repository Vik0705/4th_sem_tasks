N = int(input())
a = list(map(int, input().split()))
found = False
for i in range(1, N - 1):
    if a[i] > a[i - 1] and a[i] > a[i + 1]:
        print(a[i])
        found = True
        break
if not found:
    print("no")
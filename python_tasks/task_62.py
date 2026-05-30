N = int(input())
a = list(map(int, input().split()))
found = False
for x in a:
    if a.count(x) == 1:
        print(x, end=" ")
        found = True
if not found:
    print("no")
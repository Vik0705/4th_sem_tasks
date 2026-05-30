N = int(input())
a = list(map(int, input().split()))
res = []
for x in a:
    if x not in res:
        res.append(x)
print(*res)
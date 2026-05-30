N = int(input())
a = list(map(int, input().split()))
max_f = 0
ans = a[0]
seen = set()
for x in a:
    if x not in seen:
        seen.add(x)
        f = a.count(x)
        if f > max_f:
            max_f = f
            ans = x
print(ans, max_f)
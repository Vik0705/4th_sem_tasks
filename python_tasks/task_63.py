N = int(input())
a = list(map(int, input().split()))
max_count = 0
ans = a[0]
for x in set(a):
    c = a.count(x)
    if c > max_count:
        max_count = c
        ans = x
    elif c == max_count:
        if a.index(x) < a.index(ans):
            ans = x
print(ans)
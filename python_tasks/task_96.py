N = int(input())
a = list(map(int, input().split()))
distinct = len(set(a))
min_len = N + 1
for i in range(N):
    seen = set()
    for j in range(i, N):
        seen.add(a[j])
        if len(seen) == distinct:
            min_len = min(min_len, j - i + 1)
            break
print(min_len)
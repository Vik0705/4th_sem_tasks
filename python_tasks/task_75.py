N = int(input())
a = list(map(int, input().split()))
max_len = 0
for i in range(N):
    seen = set()
    for j in range(i, N):
        if a[j] in seen:
            break
        seen.add(a[j])
        max_len = max(max_len, len(seen))
print(max_len)
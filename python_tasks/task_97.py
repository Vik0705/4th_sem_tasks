N = int(input())
a = list(map(int, input().split()))
ans = set()
for i in range(N):
    temp = a[:i] + a[i+1:]
    if temp:
        ans.add(max(temp))
print(*sorted(list(ans)))
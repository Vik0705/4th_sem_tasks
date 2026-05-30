N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = -1
for i in range(N):
    if a[-i:] + a[:-i] == b:
        ans = i
        break
print(ans)
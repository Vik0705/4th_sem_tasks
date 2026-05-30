N = int(input())
a = list(map(int, input().split()))
seconds = set()
for i in range(N - 2):
    sub = sorted(a[i:i+3])
    seconds.add(sub[1])
print(len(seconds))
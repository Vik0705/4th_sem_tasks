N = int(input())
a = list(map(int, input().split()))
m = max(a)
first = a.index(m)
last = N - 1 - a[::-1].index(m)
if first == last:
    print(0)
else:
    print(len(set(a[first+1:last])))
N = int(input())
a = list(map(int, input().split()))

def is_nondec(lst):
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]: return False
    return True

min_rem = N
if is_nondec(a):
    min_rem = 0
else:
    for l in range(1, N + 1):
        found = False
        for i in range(N - l + 1):
            if is_nondec(a[:i] + a[i+l:]):
                found = True
                break
        if found:
            min_rem = l
            break
print(min_rem)
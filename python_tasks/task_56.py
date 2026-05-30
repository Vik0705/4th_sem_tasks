a = list(map(int, input().split()))
count = sum(1 for x in a if x % 2 == 0)
print(count)
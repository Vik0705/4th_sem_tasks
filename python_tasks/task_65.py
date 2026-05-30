N = int(input())
a = list(map(int, input().split()))
uniques = []
dupes = []
seen = set()
for x in a:
    if a.count(x) == 1:
        uniques.append(x)
    else:
        if x not in seen:
            dupes.append(x)
            seen.add(x)
print(*(uniques + dupes))
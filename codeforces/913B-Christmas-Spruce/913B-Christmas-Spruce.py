from collections import defaultdict

n = int(input())

count = defaultdict(set)
for i in range(n - 1):
    idx = int(input())

    count[idx].add(i + 2)

for key in count:
    vals = count[key]

    for k in count:
        if k in vals:
            count[key].remove(k)

for vals in count.values():
    if len(vals) < 3:
        print('No')
        break

else:
    print("Yes")
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = total = j = 0
cur = a[0]

for i in range(n):
    if a[i] != cur:
        cur = a[i]
        count = 0

    while j < m and a[i] > b[j]:
        j += 1

    while j < m and a[i] == b[j]:
        count += 1
        j += 1

    total += count
    
print(total)

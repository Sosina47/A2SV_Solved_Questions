n = int(input())
contests = list(map(int, input().split()))
contests.sort()
day = 0

for i in range(n):
    if contests[i] >= day + 1:
        day += 1

print(day) 

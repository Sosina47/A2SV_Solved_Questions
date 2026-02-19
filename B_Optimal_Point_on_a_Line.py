length = int(input())
points = list(map(int, input().split()))

points.sort()
if length % 2:
    print(points[length // 2])
else:
    print(points[length // 2 - 1])

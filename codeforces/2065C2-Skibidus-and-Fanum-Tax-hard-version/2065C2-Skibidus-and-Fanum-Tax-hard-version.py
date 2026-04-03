from bisect import bisect_left

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    b.sort()
    a[0] = min(a[0], b[0] - a[0])

    for i in range(1, n):
        if a[i - 1] > max(a[i], b[-1] - a[i]):
            print("NO")
            break

        idx = bisect_left(b, a[i - 1] + a[i])
        if idx == m:
            if a[i - 1] > a[i]:
                print("NO")
                break
            continue

        else:
            min_ = min(a[i], b[idx] - a[i])
            max_ = max(a[i], b[idx] - a[i])

            a[i] = min_ if min_ >= a[i - 1] else max_

    else:
        print("YES")
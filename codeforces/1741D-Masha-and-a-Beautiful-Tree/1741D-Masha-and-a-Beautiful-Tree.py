def merge(left, right):
    global ans 

    l = r = 0
    res = []
    swap = False

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        
        else:
            swap = True
            res.append(right[r])
            r += 1
    
    if (r == 0 or l == 0) and ans != -1:
        ans += 1 if swap else 0

    else:
        ans = -1

    res.extend(left[l:])
    res.extend(right[r:])

    return res

def mergeSort(l, r):
    if r == l:
        return [nums[l]]    
    
    mid = (l + r) // 2

    left = mergeSort(l, mid)
    right = mergeSort(mid + 1, r)

    return merge(left, right)


ans = 0

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    ans = 0
    
    mergeSort(0, n - 1)
    print(ans)
from collections import defaultdict

n, k = map(int, input().split())
nums = list(map(int, input().split()))

indices = [0, 0]
left = max_ = 0
distnict = defaultdict(int)

for right in range(n):
    distnict[nums[right]] += 1
    
    while len(distnict) > k:
        if distnict[nums[left]] == 1:
            del distnict[nums[left]]
        
        else:
            distnict[nums[left]] -= 1
        left += 1

    if max_ < right - left + 1:
        indices[0] = left + 1
        indices[1] = right + 1
        max_ = max(max_, right - left + 1)


print(*indices)

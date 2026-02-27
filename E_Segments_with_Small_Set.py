from collections import defaultdict

n, k = map(int, input().split())
nums = list(map(int, input().split()))

cur_freq = defaultdict(int)
left = count = 0

for right in range(n):
    cur_freq[nums[right]] += 1

    while len(cur_freq) > k:
        if cur_freq[nums[left]] == 1:
            del cur_freq[nums[left]]
        else:
            cur_freq[nums[left]] -= 1

        left += 1
    
    count += right - left + 1

print(count)

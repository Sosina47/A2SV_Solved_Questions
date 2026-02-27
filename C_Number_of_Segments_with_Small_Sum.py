n, s = map(int, input().split())
nums = list(map(int, input().split()))

left = count = cur = 0
for right in range(n):
    cur += nums[right]

    while cur > s:
        cur -= nums[left]
        left += 1

    count += right - left + 1

print(count)

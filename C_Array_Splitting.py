length, subarrays = map(int, input().split())
nums = list(map(int, input().split()))

diff = []
for i in range(1, length):
    diff.append(nums[i] - nums[i - 1])

diff.sort()
if subarrays == 1:
    print(sum(diff))
    
else:
    print(sum(diff[:-(subarrays - 1)]))

for _ in range(int(input())):
    length = int(input())
    nums = list(map(int, input().split()))

    count = 0
    max_ = max(nums)
    for k in range(len(nums) - 1, 1, -1):
        i, j = 0, k - 1

        while i < j:
            if nums[i] + nums[j] + nums[k] > max(max_, 2 * nums[k]):
                count += j - i
                j -= 1
            
            else:
                i += 1
    print(count)
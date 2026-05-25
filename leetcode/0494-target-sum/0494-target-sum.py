class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}

        def dp(i, total):
            if i == n:
                # print(total)
                return 1 if total == target else 0

            if(i, total) in memo: 
                return memo[(i, total)]

            plus = dp(i + 1, total + nums[i])
            minus = dp(i + 1, total - nums[i])

            # print(plus, minus)
            memo[(i, total)] = plus + minus

            return memo[(i, total)]

        dp(0, 0)
        return memo[(0, 0)]

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dp(i):
            if i >= n: 
                return 0
            
            if not i in memo:
                memo[i] = nums[i] + max(dp(i + 2), dp(i + 3))

            return memo[i]

        return max(dp(0), dp(1))
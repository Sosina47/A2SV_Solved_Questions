class Solution:
    def atmost(self, nums, k):
        count = left = cur_sum = 0
        for right in range(len(nums)):
            cur_sum += nums[right]

            while cur_sum > k:
                cur_sum -= nums[left]
                left += 1
            
            count += right - left + 1
        return count
    
    def subarraySum(self, nums: List[int], k: int) -> int:
        return self.atmost(nums, k) - self.atmost(nums, k - 1)

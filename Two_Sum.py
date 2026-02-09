class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {nums[i]: i for i in range(len(nums))}

        for i in range(len(nums)):
            if target - nums[i] in idx and i != idx[target - nums[i]]:
                return (i, idx[target - nums[i]])

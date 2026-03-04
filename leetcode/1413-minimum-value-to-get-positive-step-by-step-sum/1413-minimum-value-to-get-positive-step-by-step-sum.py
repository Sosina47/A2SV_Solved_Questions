class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        num = min(itertools.accumulate(nums))
        return 1 - num if num <= 0 else 1

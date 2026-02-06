class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        lst = Counter(nums)
        n = len(nums)
        output = []
        
        for key in lst:
            if lst[key] > n//3:
                output.append(key)

        return output

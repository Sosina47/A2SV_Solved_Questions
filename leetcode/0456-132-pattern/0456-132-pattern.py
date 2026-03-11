class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        k = [] # decreasing
        stack = [] # decreasing 

        for i in range(len(nums) - 1, -1, -1):
            while stack and stack[-1] < nums[i]:
                num = stack.pop()

                while k and k[-1] < num:
                    k.pop()
                
                k.append(num)
            
            if stack and k and nums[i] < k[0]:
                return True
            stack.append(nums[i])

        return False


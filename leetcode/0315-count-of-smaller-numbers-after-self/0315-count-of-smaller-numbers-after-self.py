class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = [(nums[i], i) for i in range(n)]
        
        smaller = defaultdict(int)

        def mergeSort(l, r):
            nonlocal smaller
            
            if l == r:
                return [nums[l]]

            mid = (l + r) // 2
            left = mergeSort(l, mid)
            right = mergeSort(mid + 1, r)

            l = r = 0
            
            while l < len(left):
                while r < len(right) and left[l][0] > right[r][0]:
                    r += 1

                smaller[left[l]] += r 
                l += 1

            while l < len(left):
                smaller[left[l]] += r
                l += 1

            return list(sorted(left + right))

        mergeSort(0, n - 1)
        
        for i in range(n):
            nums[i] = smaller[nums[i]]

        return nums
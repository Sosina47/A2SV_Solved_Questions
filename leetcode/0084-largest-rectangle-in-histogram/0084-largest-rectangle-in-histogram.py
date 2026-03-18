class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        next_smaller = defaultdict(lambda : length)
        prev_smaller = defaultdict(lambda : -1)

        stack = []
        for i in range(length):
            while stack and heights[stack[-1]] > heights[i]:
                next_smaller[stack[-1]] = i
                stack.pop()

            if stack:
                prev_smaller[i] = stack[-1]
            stack.append(i)

        max_area = 0
        for i in range(length):
            max_area = max(max_area, heights[i] * (next_smaller[i] - prev_smaller[i] - 1))

        return max_area
        

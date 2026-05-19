class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res, stack = 0, [] # stack will be pairs of (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: 
                index, height = stack.pop()
                res = max(res, height * (i - index))
                start = index
            stack.append((start, h))

        end = len(heights)
        for i, h in stack:
            res = max(res, h * (end - i))
        return res
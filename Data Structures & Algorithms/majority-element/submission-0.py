class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        major = n // 2
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
            if counts[num] > major:
                return num
        return
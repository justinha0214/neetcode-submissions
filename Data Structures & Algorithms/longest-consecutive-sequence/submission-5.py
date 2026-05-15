class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = set(nums)
        res = 0
        for n in nums:
            if (n-1) not in nums:
                curr = 0
                while (n+curr) in nums:
                    curr += 1
                    res = max(res, curr)
        return res
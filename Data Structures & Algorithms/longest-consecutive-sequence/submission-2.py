class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        ans = 0
        nums = set(nums)
        for n in nums:
            curr = 1
            if (n-1) not in nums:
                while (n+curr) in nums:
                    curr += 1
                ans = max(ans, curr)
        return ans
        
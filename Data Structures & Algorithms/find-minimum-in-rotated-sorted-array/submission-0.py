class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = min(nums[0], nums[-1])
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + ((r-l) // 2)
            if nums[mid] < res:
                r = mid - 1
            else:
                l = mid + 1
            res = min(res, nums[mid])
        return res
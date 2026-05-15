class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        for i in range(len(nums)):
            start, product = 0, 1
            while start < len(nums):
                if start != i:
                    product = product * nums[start]
                start += 1
            ans[i] = product
        return ans

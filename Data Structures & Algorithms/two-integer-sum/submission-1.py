class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, n in enumerate(nums):
            cur = target - n
            if cur in hashMap:
                return [hashMap[cur], i]
            hashMap[n] = i
        
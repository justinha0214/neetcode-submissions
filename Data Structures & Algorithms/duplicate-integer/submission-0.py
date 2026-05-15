class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for n in nums:
            if n in hashMap:
                return True
            hashMap[n] = 1
        return False
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        
        minVal, maxVal = min(nums), max(nums)
        i = 0
        for val in range(minVal, maxVal + 1):
            while counts[val] > 0:
                nums[i] = val
                i += 1
                counts[val] -= 1
        return nums


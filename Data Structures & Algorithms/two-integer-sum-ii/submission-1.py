class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            add = numbers[r] + numbers[l]
            if add == target:
                return [l+1, r+1]
            elif add > target:
                r -= 1
            elif add < target:
                l += 1
        return 
            
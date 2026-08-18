class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bst(nums, target, left, right):
            if left > right:
                return -1
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return bst(nums, target, left, mid - 1)
            else: # nums[mid] < target
                return bst(nums, target, mid + 1, right)
        
        return bst(nums, target, 0, len(nums) - 1)

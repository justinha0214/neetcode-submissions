class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bst(l, r):
            if l > r:
                return -1
            
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return bst(mid + 1, r)
            else:
                return bst(l, mid - 1)
        
        return bst(0, len(nums) - 1)

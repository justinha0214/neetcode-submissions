class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def bst(nums: List[int], target: int) -> bool:
            l, r = 0, len(nums) - 1
            while l <= r:
                m = l + ((r - l) // 2)
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    return True
            return False
        
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m - 1
        while l <= r:
            mid = l + ((r-l) // 2)
            if target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0]: 
                r = mid - 1
            else:
                return bst(matrix[mid], target) 
        
        return False
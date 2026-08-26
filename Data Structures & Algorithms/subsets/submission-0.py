class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                ans.append(subset.copy())
                return
            
            # Left side of decision tree to include i and continue
            subset.append(nums[i])
            dfs(i+1)

            # Pop the value and continue DFS without i, right side of tree
            subset.pop()
            dfs(i+1)

        dfs(0)
        return ans

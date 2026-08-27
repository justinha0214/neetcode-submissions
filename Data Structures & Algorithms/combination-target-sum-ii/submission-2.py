class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        candidates.sort()

        def dfs(i, combo, total):
            if total == target: 
                ans.add(tuple(combo))
                return
            elif i >= len(candidates) or total > target:
                return
            
            combo.append(candidates[i])
            dfs(i + 1, combo, total + candidates[i])

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            combo.pop()
            dfs(i+1, combo, total)
        
        dfs(0, [], 0)
        return [list(combination) for combination in ans]
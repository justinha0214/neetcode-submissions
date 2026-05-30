class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):
            if row >= 0 and col >= 0 and row < rows and col < cols and grid[row][col] == "1":
                grid[row][col] = "0"
                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    res += 1 
                    dfs(r, c)
        return res
        
        
                
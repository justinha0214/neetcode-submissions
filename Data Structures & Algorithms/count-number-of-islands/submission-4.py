class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(x, y):
            if x not in range(0, ROWS) or y not in range(0, COLS) or grid[x][y] == '0':
                return
            grid[x][y] = '0'
            for dr, dc in directions:
                dfs(x+dr, y+dc)
        
        count = 0
        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == '1':
                    count += 1
                    dfs(x, y)
        return count
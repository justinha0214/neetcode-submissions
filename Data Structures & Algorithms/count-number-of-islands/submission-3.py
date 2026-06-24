class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        rows = len(grid)
        cols = len(grid[0])

        def islands(row, col):
            if row >= rows or col >= cols or row < 0 or col < 0 or grid[row][col] == "0":
                return
            else:
                grid[row][col] = "0"
                for l, r in directions:
                    islands(row + l, col + r)
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands(r, c)
                    res += 1
        return res
        
        
                
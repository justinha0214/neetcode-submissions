class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(row, col, prevHeight, visited):
            if ((row,col) in visited or
                row < 0 or
                col < 0 or
                row == ROWS or
                col == COLS or
                prevHeight > heights[row][col]):
                return
            
            visited.add((row,col))
            for dr, dc in directions:
                dfs(row + dr, col + dc, heights[row][col], visited)
        
        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, COLS - 1, heights[r][COLS - 1], atl)
        for c in range(COLS):
            dfs(0, c, heights[0][c], pac)
            dfs(ROWS - 1, c, heights[ROWS-1][c], atl)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res

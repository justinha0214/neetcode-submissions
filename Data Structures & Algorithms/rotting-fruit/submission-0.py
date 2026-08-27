class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]

        fresh, rotten = 0, deque()
        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == 1:
                    fresh += 1
                if grid[x][y] == 2:
                    rotten.append([x,y])
        
        time = 0
        while fresh > 0 and rotten:
            length = len(rotten)
            for i in range(length):
                x,y = rotten.popleft()
                for dr, dc in directions:
                    row, col = x + dr, y + dc
                    if row in range(ROWS) and col in range(COLS) and grid[row][col] == 1:
                        grid[row][col] = 2
                        rotten.append([row, col])
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1
        
        
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        maxarea = 0

        def dfs(row, col):
            
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != 1:
                return 0
            area=1
            grid[row][col] = 0
            area += dfs(row + 1, col)
            area += dfs(row - 1, col)
            area += dfs(row, col + 1)
            area += dfs(row, col - 1)

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxarea = max(maxarea, dfs(r, c))
        return maxarea

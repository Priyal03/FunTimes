class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        # visited = set()
        closedIsland = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= (m) or col >= (n):
                return False
            if grid[row][col] == 1:
                return True
            grid[row][col] = 1
            #we must traverese to the depth in all directions and mark them visited and then if true we get the correct Island
            possible = True
            possible &= dfs(row - 1, col)
            possible &= dfs(row + 1, col)
            possible &= dfs(row, col - 1)
            possible &= dfs(row, col + 1)
            return possible

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if dfs(i, j):
                        closedIsland += 1

        return closedIsland

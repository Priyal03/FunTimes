class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
                return False
            if (i, j) in visited:
                return False
            else:
                visited.add((i, j))
                if grid[i][j] == "1":
                    dfs(i + 1, j)
                    dfs(i - 1, j)
                    dfs(i, j - 1)
                    dfs(i, j + 1)
                return True     

        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    if dfs(i, j):
                        islands += 1

        return islands
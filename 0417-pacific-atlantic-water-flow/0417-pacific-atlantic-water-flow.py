class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(row, col, visited):
            visited.add((row, col))
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                newrow = x + row
                newcol = y + col
                if newrow < 0 or newrow >= m or newcol < 0 or newcol >= n:
                    continue
                if (newrow, newcol) in visited:
                    continue
                if heights[newrow][newcol] < heights[row][col]:
                    continue
                dfs(newrow, newcol, visited)

        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n - 1, atlantic)

        for j in range(n):
            dfs(0, j, pacific)
            dfs(m - 1, j, atlantic)

        return list(pacific.intersection(atlantic))

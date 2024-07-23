class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        visited = set()

        def dfs(i, j):
            if (
                i < 0
                or i >= m
                or j < 0
                or j >= n
                or (i, j) in visited
                or grid2[i][j] == 0
            ):
                return True
                
            if grid1[i][j] == 0:
                return False
            
            itsOne = True
            
            visited.add((i, j))
            itsOne &= dfs(i + 1, j)
            itsOne &= dfs(i - 1, j)
            itsOne &= dfs(i, j - 1)
            itsOne &= dfs(i, j + 1)
                
            return itsOne

        subIslands = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and (i, j) not in visited:
                    if dfs(i, j):
                        subIslands += 1

        return subIslands

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(row, col):
            if row<0 or row>=m or col<0 or col>=n or grid[row][col]==0:
                return
            if grid[row][col]==1:
                grid[row][col]=0
            dfs(row-1,col)
            dfs(row+1,col)
            dfs(row,col-1)
            dfs(row,col+1)

        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
        for j in range(n):
            dfs(0,j)
            dfs(m-1,j)
        
        enclaves=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    enclaves+=1

        return enclaves
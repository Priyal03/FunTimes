class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        self.perimeter=0

        def removeCommonWall(row, col):
            if row<0 or col<0 or row>=m or col >= n or grid[row][col]==0:
                return
            self.perimeter-=1

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    self.perimeter+=4
                    removeCommonWall(i-1,j)
                    removeCommonWall(i+1,j)
                    removeCommonWall(i,j+1)
                    removeCommonWall(i,j-1)
        return self.perimeter
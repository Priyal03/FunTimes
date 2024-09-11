class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total=0
        rows=len(grid)
        cols=len(grid[0])
        if not grid:
            return 0
        queue=deque([])
        directions=[(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    queue.append((r,c))
                    grid[r][c]="0"
                    while queue:
                        x,y=queue.popleft()
                        for d in directions:
                            nx = x+d[0]
                            ny= y+d[1]
                            if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]=="1":
                                queue.append((nx,ny))
                                grid[nx][ny]="0"
                    total+=1

        return total
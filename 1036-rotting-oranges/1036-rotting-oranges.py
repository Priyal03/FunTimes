class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        fresh = 0
        queue = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        minute = 0
        while queue and fresh > 0:
            minute += 1

            for k in range(len(queue)):
                i, j = queue.popleft() # i = row, j=col

                for dx,dy in directions:
                    row, col = i + dx, j + dy
                    if 0 <= row < n and 0 <= col < m:
                        if grid[row][col] == 1:
                            grid[row][col] = 2
                            fresh -= 1
                            queue.append((row, col))

        return -1 if fresh > 0 else minute

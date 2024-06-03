class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1
        minutes = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue and fresh>0:
            minutes += 1
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for d in directions:
                    nrow, ncol = row + d[0], col + d[1]
                    if rows > nrow >= 0 and cols > ncol >= 0:
                        if grid[nrow][ncol] == 1:
                            grid[nrow][ncol] = 2
                            fresh -= 1
                            queue.append((nrow, ncol))
        return minutes if fresh == 0 else -1
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        def dfs(i, j):
            if i < 0 or i >= (m) or j < 0 or j >= (n) or board[i][j] != "O":
                return
            # marking the border Os to be safe with $
            board[i][j] = "#"
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)
            
        # revert the $ to safe Os and surrounded region Os to Xs
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"  # Surrounded 'O', capture it
                elif board[i][j] == "#":
                    board[i][j] = "O"  # Restore border 'O'

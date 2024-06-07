class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(row, col, curr, i):
            if i == len(word):
                return True
            if (
                row < 0
                or col < 0
                or row >= rows
                or col >= cols
                or board[row][col] != word[i]
            ):
                return False

            temp = board[row][col]
            board[row][col] = "$"

            found = (dfs(row + 1, col, curr + word[i], i + 1)
                or dfs(row - 1, col, curr + word[i], i + 1)
                or dfs(row, col + 1, curr + word[i], i + 1)
                or dfs(row, col - 1, curr + word[i], i + 1))
            board[row][col] = temp
            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, "", 0):
                    return True
        return False

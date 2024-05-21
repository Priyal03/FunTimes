class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = [set() for _ in range(9)]
        colset = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                if board[row][col]!=".":
                    
                    if board[row][col] in rowset[row]:
                        return False
                    rowset[row].add(board[row][col])
                    if board[row][col] in colset[col]:
                        return False
                    colset[col].add(board[row][col])

                    index = (row//3)*3+(col//3)
                    if board[row][col] in boxes[index]:
                        return False
                    boxes[index].add(board[row][col])

        return True
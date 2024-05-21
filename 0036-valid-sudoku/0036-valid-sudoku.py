class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n=9
        rowset = [[0]*n for _ in range(9)]
        colset = [[0]*n for _ in range(9)]
        boxes = [[0]*n for _ in range(9)]
        for row in range(9):
            for col in range(9):
                if board[row][col]!=".":
                    id = int(board[row][col])-1
                    if rowset[row][id] == 1:
                        return False
                    rowset[row][id]=1
                    if colset[col][id]==1:
                        return False
                    colset[col][id]=1

                    index = (row//3)*3+(col//3)
                    if boxes[index][id]==1:
                        return False
                    boxes[index][id]=1

        return True
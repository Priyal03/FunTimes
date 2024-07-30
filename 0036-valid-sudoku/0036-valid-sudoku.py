class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [0]*9
        col = [0]*9
        box = [0]*9

        for i in range(9):
            for j in range(9):
                
                num = board[i][j]
                if num=='.':
                    continue
                
                num=int(num)-1
                boxIndex = i//3 + (j//3)*3
                bit = 1<<num
                
                if row[i] & bit or col[j] & bit or box[boxIndex]&bit:
                    return False

                row[i] |= bit
                col[j]|=bit
                box[boxIndex]|=bit

        return True
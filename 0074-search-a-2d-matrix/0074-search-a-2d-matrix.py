class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        if rows == 0:
            return False
        cols = len(matrix[0])

        left=0
        right = rows*cols -1
        
        while left<=right:
            #virtual array index
            index = (left+right)//2
            #mapping from the 2D matrix based on cols as it is stored in row manner.
            midElement = matrix[index//cols][index%cols]

            if target == midElement:
                return True
            else:
                if target<midElement:
                    right = index-1
                else:
                    left = index+1
        return False
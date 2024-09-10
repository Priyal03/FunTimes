class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        n=len(board)
        #function to convert 1d number to 2d position in matrix
        def get_board_coordinates(value):
            r = (value-1)//n 
            c = (value-1)%n
            if r%2==1:
                c=n-1-c #reversing direction for odd rows
            return n-1-r,c #fliping the row for bottom to top layout.
        
        queue= deque([(1,0)]) #current square and steps taken
        visited =set([1]) #starts at square 1

        while queue:
            square, steps = queue.popleft()
            if square == n*n:
                return steps
            for i in range(1,7):
                next_square = square+i
                if next_square > n*n:
                    continue
                r,c=get_board_coordinates(next_square)
                if board[r][c]!=-1:
                    next_square=board[r][c]
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square,steps+1))
        return -1
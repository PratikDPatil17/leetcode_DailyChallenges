class Solution(object):
    def gameOfLife(self, board):
        # Original   |  New  |  State
        #     0      |   0   |    0
        #     1      |   0   |    1
        #     0      |   1   |    2
        #     1      |   1   |    3
        
        ROWS, COLS = len(board), len(board[0])
       # Helper function just to count neighbours of each cell in board 
        def countNeighbours(r,c):
            nCount = 0
            for i in range(r-1, r+2):
                for j in range(c-1,c+2):
                    if ((i == r and j == c) or i<0 or j<0 or i == ROWS or j == COLS):
                        continue
                    if board[i][j] in [1,3]:
                        nCount += 1
                        
            return nCount
                    
        # update in place values as per rules and above truth table      
        for r in range(ROWS):
            for c in range(COLS):
                nCount = countNeighbours(r,c)
                
                if board[r][c]:
                    if nCount in [2,3]:
                        board[r][c] = 3
                        
                elif nCount == 3:
                    board[r][c] = 2
        # replace values as per above truth table in place to achieve SC= O(1)...           
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 1:
                    board[r][c] = 0
                elif board[r][c] in [2,3]:
                    board[r][c] = 1
        
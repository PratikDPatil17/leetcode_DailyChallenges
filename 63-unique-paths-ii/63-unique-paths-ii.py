class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1:
            return 0
        
        #number of ways of reaching the startiing cell = 1
        obstacleGrid[0][0] = 1
        
        #filling the values for first col
        for i in range(1,m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)
            
        #filling the values for second row
        for j in range(1,n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)
            
        
        #starting from cell(1,1) now fill up the values
        #No of ways reaching cell[i][j] = cell[i-1][j] + cell[i][j-1]
        # i.e from above + left
        
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
                    
        return obstacleGrid[m-1][n-1]
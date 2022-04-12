class Solution(object):
    def shiftGrid(self, grid, k):
        M,N = len(grid), len(grid[0])
        
        # Helper functions
        def posToVal(r,c):
            return r*N + c
        
        def valToPos(V):
            return [V // N, V % N]
        
        res = [[0]*N for i in range(M)]
        for r in range(M):
            for c in range(N):
                newVal = (posToVal(r,c) + k) % (M*N)
                
                newR, newC = valToPos(newVal)
                res[newR][newC] = grid[r][c]
                
        return res
                
        
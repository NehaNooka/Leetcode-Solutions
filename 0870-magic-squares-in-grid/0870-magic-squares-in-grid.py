class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        res=0
        if len(grid)< 3 or len(grid[0])<3:
            return 0
        def helper(i,j):
            if (grid[i][j] + grid[i][j+1] + grid[i][j+2] ==
                grid[i+1][j] + grid[i+1][j+1]+ grid[i+1][j+2] ==
                grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2] ==
                grid [i][j] + grid[i+1][j] + grid[i+2][j] ==
                grid[i][j+1] + grid[i+1][j+1]+ grid[i+2][j+1] ==
                grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2] ==
                grid[i][j]+grid[i+1][j+1]+grid[i+2][j+2] ==
                grid[i+2][j]+grid[i+1][j+1]+grid[i][j+2]) and (grid[i][j] != grid[i][j+1] != grid[i][j+2] !=
                grid[i+1][j] != grid[i+1][j+1]!= grid[i+1][j+2] != 
                grid[i+2][j] != grid[i+2][j+1] != grid[i+2][j+2]) and (0< grid[i][j] < 10 and 0<grid[i][j+1] < 10 and 0<grid[i][j+2] < 10 and
                0<grid[i+1][j] < 10 and 0<grid[i+1][j+1]< 10 and 0<grid[i+1][j+2] < 10 and 
                0<grid[i+2][j] < 10 and 0<grid[i+2][j+1]< 10 and 0<grid[i+2][j+2]< 10):
                return 1
            else: return 0
        for i in range(0,len(grid)-2):
            for j in range(0,len(grid[0])-2):
                res+=helper(i,j)
        
        return res
        

            

        
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        for j in range(cols-2, -1,-1):
            grid[rows-1][j]=grid[rows-1][j]+grid[rows-1][j+1]
        for i in range(rows-2,-1,-1):
            grid[i][cols-1] = grid[i][cols-1] + grid[i+1][cols-1]
        
        for i in range(rows-2,-1,-1):
            for j in range(cols-2,-1,-1):
                grid[i][j]= grid[i][j]+ min(grid[i][j+1],grid[i+1][j])
                
        return grid[0][0]



        


        
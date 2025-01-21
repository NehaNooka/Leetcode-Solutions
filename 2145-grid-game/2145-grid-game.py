class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        N=len(grid[0])
        preRow1,preRow2=grid[0].copy(),grid[1].copy()

        for i in range(1,N):
            preRow1[i]+=preRow1[i-1]
            preRow2[i]+=preRow2[i-1]
        
        res=float('inf')
        for i in range(N):
            top=preRow1[-1]-preRow1[i]
            bot=preRow2[i-1] if i>0 else 0
            secondRobot=max(top,bot)
            res=min(res,secondRobot)
        return res

        
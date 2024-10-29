class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        directions=[[0,1],[1,1],[-1,1]]
        
        @cache
        def dp(r,c):
            res=0
            for dr,dc in directions:
                new_r,new_c=r+dr,c+dc
                if 0<=new_r<R and 0<=new_c<C and grid[r][c]< grid[new_r][new_c]:
                    res=max(res,1+dp(new_r,new_c))
            return res

        return max(dp(r,0) for r in range(R))

        
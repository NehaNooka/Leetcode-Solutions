class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ROW,COL=len(grid),len(grid[0])
        visit=set()
        def bfs(r,c):
            if r<0 or c<0 or r==ROW or c==COL or grid[r][c]==0 or (r,c) in visit: return 0

            visit.add((r,c))
            res=grid[r][c]+bfs(r+1,c)+bfs(r-1,c)+bfs(r,c+1)+bfs(r,c-1)
            return res
        res=0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]>0 and (r,c) not in visit:
                    res=max(res,bfs(r,c))
        return res

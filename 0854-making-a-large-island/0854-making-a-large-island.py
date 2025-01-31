class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        N=len(grid)

        def dfs(r,c,label):
            if r<0 or c<0 or r==N or c==N or grid[r][c]!=1: return 0
            grid[r][c]=label
            res=1
            nei=[[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
            for nr,nc in nei:
                res+=dfs(nr,nc,label)
            return res
            
        size=defaultdict(int)
        label=2
        for r in range(N):
            for c in range(N):
                if grid[r][c]==1:
                    size[label]=dfs(r,c,label)
                    label+=1
        
        def compute(r,c):
            nei=[[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
            visit=set()
            res=1
            for nr,nc in nei:
                if not(nr<0 or nc<0 or nr==N or nc==N) and grid[nr][nc] not in visit:
                    res+=size[grid[nr][nc]]
                    visit.add(grid[nr][nc])
            return res

        res=0 if not size else max(size.values())
        for r in range(N):
            for c in range(N):
                if grid[r][c]==0:
                    res=max(res,compute(r,c))
        return res


        


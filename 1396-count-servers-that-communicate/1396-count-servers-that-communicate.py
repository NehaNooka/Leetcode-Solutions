class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        computers=[]
        row,col=[0]*n,[0]*m

        for r in range(n):
            for c in range(m):
                if grid[r][c]:
                    computers.append((r,c))
                    row[r]+=1
                    col[c]+=1
            
        res=0
        for r,c in computers:
            if row[r]>1 or col[c]>1:
                res+=1
        return res
        
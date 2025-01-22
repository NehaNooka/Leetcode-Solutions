class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q=deque()
        R,C=len(isWater),len(isWater[0])
        res=[[-1]*C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                if isWater[r][c]==1:
                    res[r][c]=0
                    q.append((r,c))

        direction=[[1,0],[-1,0],[0,-1],[0,1]]        
        while q:
            i,j=q.popleft()
            for dr,dc in direction:
                r,c=i+dr,j+dc
                if r<0 or c<0 or r==R or c==C or res[r][c]!=-1: continue
                res[r][c]=res[i][j]+1
                q.append((r,c))

        return res
        


        
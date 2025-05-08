class Solution:
    def minTimeToReach(self, arr: List[List[int]]) -> int:
        m,n=len(arr),len(arr[0])
        dp=[[math.inf for i in range(n)] for j in range(m)]

        he=[]
        heappush(he,(0,1,0,0))
        vis=set()
        dirs=[(0,1),(1,0),(0,-1),(-1,0)]

        while he:
            t,cost,x,y=heappop(he)
            if x==m-1 and y==n-1:
                return t

            for xx,yy in dirs:
                i,j=x+xx,y+yy

                if 0<=i<m and 0<=j<n and (i,j,cost) not in vis:
                    newtime=max(t,arr[i][j])+cost
                    vis.add((i,j,cost))
                    newcost = 1 if cost==2 else 2
                    heappush(he, (newtime, newcost , i, j))
            
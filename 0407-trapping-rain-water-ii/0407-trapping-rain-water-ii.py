class Solution:
    def trapRainWater(self, height: List[List[int]]) -> int:
        ROWS,COLS=len(height),len(height[0])
        
        #1. Add borders to min,Heap -> then mark as visited
        min_heap=[] # height,r,c
        for r in range(ROWS):
            for c in range(COLS):
                if r in [0,ROWS-1] or c in [0,COLS-1]:
                    heapq.heappush(min_heap,(height[r][c],r,c))
                    height[r][c]=-1
        
        #2. Prioritize smaller heights-> Maintain max height to calculate water stored in each inner cells
        res,max_h=0,-1
        while min_heap:
            h,r,c=heapq.heappop(min_heap)
            max_h=max(max_h,h)
            res+=max_h-h

            neighbors=[[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
            for nr,nc in neighbors:
                if (nr<0 or nr==ROWS or nc<0 or nc==COLS or height[nr][nc]==-1): continue
                heapq.heappush(min_heap,(height[nr][nc],nr,nc))
                height[nr][nc]=-1
        return res
 

        
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:

        ROWS,COLS=len(grid),len(grid[0])
        visit=set()
        minHeap=[(0,0,0)]
        while minHeap:
            obs,r,c = heapq.heappop(minHeap)
            if (r,c)==(ROWS-1,COLS-1): return obs
            nei=[(r+1,c),(r-1,c),(r,c+1),(r,c-1)]

            for nr,nc in nei:
                if (nr,nc) in visit or nr<0 or nc<0 or nr==ROWS or nc==COLS:
                    continue
                visit.add((nr,nc))
                heapq.heappush(minHeap,(obs+grid[nr][nc],nr,nc))
        



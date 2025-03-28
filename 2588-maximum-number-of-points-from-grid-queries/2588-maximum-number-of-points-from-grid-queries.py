class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        sorted_q = sorted(queries)
        m,n=len(grid),len(grid[0])
        query_res={}
        res=[0]*len(queries)

        d=[(0,1),(0,-1),(1,0),(-1,0)]
        minHeap=[(grid[0][0],0,0)]
        visit=set()
        visit.add((0,0))

        points=0

        for q in sorted_q:
            while minHeap and minHeap[0][0]< q:
                val,r,c=heapq.heappop(minHeap)
                points+=1

                for dr,dc in d:
                    nr,nc=r+dr,c+dc

                    if 0<=nr<m and 0<=nc<n and (nr,nc) not in visit:
                        heapq.heappush(minHeap,(grid[nr][nc],nr,nc))
                        visit.add((nr,nc))
            query_res[q]=points

        for i,q in enumerate(queries):
            res[i]=query_res[q]
        
        return res
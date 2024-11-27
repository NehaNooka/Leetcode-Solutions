class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj={}
        for i in range(n-1):
            adj[i]=[i+1]

        def bfs():
            minHeap=[(0,0)]
            distances=[inf]*n
            distances[0]=[0]
            while minHeap:
                w,i=heapq.heappop(minHeap)
                if i==n-1:
                    return w
                for edge in adj[i]:
                    new_w=w+1
                    if (w+1)<distances[edge]:
                        distances[edge]=w+1
                        heapq.heappush(minHeap,(w+1,edge))

        res=[]
        for u,v in queries:
            adj[u].append(v)
            res.append(bfs())
        return res

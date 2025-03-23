class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj=defaultdict(list)
        for u,v,time in roads:
            adj[u].append((v,time))
            adj[v].append((u,time))
        
        dist=[0]+[float('inf')]*(n-1)
        ways=[1]+[0]*(n-1)

        pq=[(0,0)] #(time,node)
        MOD=10**9+7

        #Dijkstra's Algo
        while pq:
            d,node=heapq.heappop(pq)

            if d>dist[node]:
                continue
            
            for nei,t in adj[node]:
                if dist[node]+t<dist[nei]:
                    dist[nei]=dist[node]+t
                    ways[nei]=ways[node]
                    heapq.heappush(pq,(dist[nei],nei))
                elif dist[node]+t==dist[nei]:
                    ways[nei]=(ways[nei]+ways[node])%MOD
                    
        return ways[n-1]



        
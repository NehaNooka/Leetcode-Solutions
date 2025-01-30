class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj=defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def longest_path(src):
            q=deque([(src,1)])
            dist={src:1}
            while q:
                node,length=q.popleft()
                for nei in adj[node]:
                    if nei in dist:
                        if dist[nei]==length: return None,-1
                        continue
                    
                    q.append((nei,length+1))
                    visit.add(nei)
                    dist[nei]=length+1
            return dist,max(dist.values())
        visit=set()
        res=0
        for i in range(1,n+1):
            if i in visit:
                continue
            visit.add(i)

            component,length=longest_path(i)
            if length==-1: return -1
            max_cnt=0
            for src in component:
                _,length=longest_path(src)
                max_cnt=max(max_cnt,length)
            res+=max_cnt
        return res


        
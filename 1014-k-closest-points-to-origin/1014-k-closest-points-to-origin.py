class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist=[]
        for x,y in points:
            dist.append((x**2+y**2,[x,y]))
        heapq.heapify(dist)
        res=[]
        while k:
            point=heapq.heappop(dist)
            res.append(point[1])
            k-=1
        return res
        
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res,maxHeap='',[]
        for count,key in [(-a,'a'),(-b,'b'),(-c,'c')]:
            if count!=0:
                heapq.heappush(maxHeap,(count,key))
        
        while maxHeap:
            count,key=heapq.heappop(maxHeap)
            if len(res)>1 and res[-1]==res[-2]==key:
                if not maxHeap:
                    return res
                count2,key2=heapq.heappop(maxHeap)
                res+=key2
                count2+=1
                if count2:
                    heapq.heappush(maxHeap,(count2,key2))
            else:
                res+=key
                count+=1
            if count:
                heapq.heappush(maxHeap,(count,key))
        return res




        
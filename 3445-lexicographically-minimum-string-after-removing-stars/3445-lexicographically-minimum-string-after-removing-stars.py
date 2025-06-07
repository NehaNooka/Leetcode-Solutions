class Solution:
    def clearStars(self, s: str) -> str:
        heap=[]
        deleted=set()

        for i,c in enumerate(s):
            if c=='*':
                c,neg_idx=heapq.heappop(heap)
                deleted.add(-neg_idx)
            else:
                heapq.heappush(heap,(c,-i))
        res=[]
        for i,c in enumerate(s):
            if i in deleted or c=='*': continue
            res.append(c)
        return ''.join(res)


        
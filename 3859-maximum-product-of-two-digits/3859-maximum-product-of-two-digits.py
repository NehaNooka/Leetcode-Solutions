class Solution:
    def maxProduct(self, n: int) -> int:
        newN=[]
        for i in str(n):
            heapq.heappush(newN,-int(i))
        a=heapq.heappop(newN)
        b=heapq.heappop(newN)
        return a*b

        
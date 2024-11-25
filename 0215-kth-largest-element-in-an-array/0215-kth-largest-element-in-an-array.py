class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        num=[]
        for n in nums:
            heapq.heappush(num,-n)
        while k>0:
            n=-1*heapq.heappop(num)
            k-=1
        return n
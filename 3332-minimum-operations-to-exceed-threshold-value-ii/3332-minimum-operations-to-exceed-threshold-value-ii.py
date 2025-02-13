class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res=0
        while len(nums)>1 and nums[0]<k:
            x=heapq.heappop(nums)
            y=heapq.heappop(nums)
            new= x*2 + y
            heapq.heappush(nums,new)
            res+=1
        return res if nums[0]>=k else -1
        
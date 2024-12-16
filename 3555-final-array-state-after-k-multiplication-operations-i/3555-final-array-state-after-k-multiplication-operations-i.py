class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        min_heap=[]
        for index,value in enumerate(nums):
            heapq.heappush(min_heap,(value,index))
        
        while k:
            val,idx=heapq.heappop(min_heap)
            nums[idx]=val*multiplier
            heapq.heappush(min_heap,(nums[idx],idx))
            k-=1
        return nums

        
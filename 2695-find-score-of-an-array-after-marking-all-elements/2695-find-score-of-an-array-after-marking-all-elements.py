class Solution:
    def findScore(self, nums: List[int]) -> int:
        nums_arr=[]
        for i,v in enumerate(nums):
            nums_arr.append((v,i))
        heapq.heapify(nums_arr)
        ans,marked=0,set()
        while nums_arr:
            val,idx=heapq.heappop(nums_arr)
            if idx not in marked:
                ans+=val
                marked.add(idx)
                marked.add(idx+1)
                marked.add(idx-1)
        return ans

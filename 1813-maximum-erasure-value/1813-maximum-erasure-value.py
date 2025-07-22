class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res,l,curSum=0,0,0
        curSet=set()
        for r in range(len(nums)):
            while nums[r] in curSet:
                curSet.remove(nums[l])
                curSum-=nums[l]
                l+=1
            curSet.add(nums[r])
            curSum+=nums[r]
            res=max(res,curSum)
        return res
            
        
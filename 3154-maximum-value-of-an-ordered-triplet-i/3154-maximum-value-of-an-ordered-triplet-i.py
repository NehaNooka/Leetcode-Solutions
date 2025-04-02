class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]-nums[j]<=0: continue
                for k in range(j+1,len(nums)):
                    val=(nums[i]-nums[j])*nums[k]
                    res=max(res,val)
        return res
        
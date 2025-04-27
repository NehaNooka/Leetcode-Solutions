class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        res=0
        l=0
        for r in range(2,len(nums)):
            if nums[l]+nums[r]==nums[l+1]/2:
                res+=1
            l+=1
        return res
        
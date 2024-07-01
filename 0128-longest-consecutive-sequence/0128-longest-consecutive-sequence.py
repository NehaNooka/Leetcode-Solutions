class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)==1:
            return 1
        if len(nums)==0:
            return 0
        res=1
        ans=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                res+=1
                ans=max(ans,res)
            elif nums[i]==nums[i-1]:
                continue
            else:
                ans=max(ans,res)
                res=1
        return ans
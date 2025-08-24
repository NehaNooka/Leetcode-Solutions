class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0
        res=0
        zeroes=0
        for r in range(len(nums)):
            if nums[r]==0: zeroes+=1
            while zeroes>1:
                if nums[l]==0: zeroes-=1
                l+=1
            res=max(res,r-l)
        return res

        
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=res=zeroes_count=0
        for r in range(len(nums)):
            if nums[r]==0:
                zeroes_count+=1
            
            while zeroes_count>k:
                if nums[l]==0:
                    zeroes_count-=1
                l+=1          
            res=max(res,r-l+1)

        return res


        
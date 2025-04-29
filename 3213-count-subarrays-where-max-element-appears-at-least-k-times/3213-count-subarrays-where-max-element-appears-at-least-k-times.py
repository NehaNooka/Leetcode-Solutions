class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_nums,res,l,count= max(nums),0,0,0

        for r in range(len(nums)):
            count+= nums[r]==max_nums

            while count>=k:
                res+= len(nums)-r
                if nums[l]==max_nums:
                    count-=1
                l+=1
        return res
            

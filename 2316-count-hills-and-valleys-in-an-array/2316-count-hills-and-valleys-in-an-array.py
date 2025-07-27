class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        prev,res=nums[0],0
        for i in range(1,len(nums)-1):
            if (nums[i]>prev and nums[i]>nums[i+1]) or (nums[i]<prev and nums[i]<nums[i+1]): 
                res+=1
                prev=nums[i]
        return res


        
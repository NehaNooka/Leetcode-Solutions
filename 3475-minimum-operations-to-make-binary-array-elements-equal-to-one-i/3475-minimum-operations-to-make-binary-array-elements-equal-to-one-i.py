class Solution:
    def minOperations(self, nums: List[int]) -> int:
        op=0
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i]= 1
                if (i+1)<len(nums): nums[i+1]^=1
                else: return -1
                if (i+2)<len(nums): nums[i+2]^=1
                else: return -1
                op+=1
        return op
        
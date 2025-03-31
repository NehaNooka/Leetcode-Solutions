class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1: return nums[0]
        res=[0]*n
        res[0]=nums[0]
        res[1]=max(nums[0],nums[1])
        for n in range(2,n):
            res[n]=max(res[n-1],nums[n]+res[n-2])
        return res[-1]
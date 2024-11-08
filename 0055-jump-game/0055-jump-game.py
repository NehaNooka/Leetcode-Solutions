class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump=len(nums)-1

        for i in range(len(nums)-1,-1,-1):
            if i+nums[i]>=jump:
                jump=i
        return True if jump==0 else False        
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1,rob2=0,0
        for n in range(len(nums)):
            temp=max(rob1+nums[n], rob2)
            rob1=rob2
            rob2=temp
        return rob2
        
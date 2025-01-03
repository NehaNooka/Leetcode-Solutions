class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        res=0
        leftCount=0
        rightCount=sum(nums)
        for i in range(len(nums)-1):
            leftCount+=nums[i]
            rightCount-=nums[i]
            if leftCount>=rightCount:
                res+=1
        return res
        
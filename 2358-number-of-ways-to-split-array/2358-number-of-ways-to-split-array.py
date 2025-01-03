class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        res=0
        rightCount=0
        leftCount=sum(nums)
        for i in range(len(nums)-1):
            rightCount+=nums[i]
            leftCount-=nums[i]
            if rightCount>=leftCount:
                res+=1
        return res
        
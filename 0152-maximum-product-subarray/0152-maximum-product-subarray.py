class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        maxP,minP=1,1

        for i in nums:
            if i==0:
                maxP,minP=1,1
                continue
            temp=maxP
            maxP=max(maxP*i,i,minP*i)
            minP=min(minP*i,i,temp*i)
            res=max(res,maxP)
        return res

        
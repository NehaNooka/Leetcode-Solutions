class Solution:
    def maxProduct(self, nums: List[int]) -> int:   
        res=max(nums)
        curMax,curMin=1,1

        for n in nums:
            if n==0:
                curMax,curMin=1,1
                continue
            tmp=curMax
            curMax=max(curMax*n,curMin*n, n)
            curMin=min(curMin*n,tmp*n,n)
            res=max(res,curMax)
        return res

        
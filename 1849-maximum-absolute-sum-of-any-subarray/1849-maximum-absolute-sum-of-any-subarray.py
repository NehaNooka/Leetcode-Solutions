class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_pre,max_pre,res,cur=0,0,0,0
        for n in nums:
            cur+=n
            res=max(res,abs(cur-min_pre),abs(cur-max_pre))
            min_pre=min(min_pre,cur)
            max_pre=max(max_pre,cur)
        return res
        
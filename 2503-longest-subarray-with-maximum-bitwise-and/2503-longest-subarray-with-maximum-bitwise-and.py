class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        size,res=0,0
        cur_max=0
        for n in nums:
            if n > cur_max:
                cur_max=n
                size=1
                res=0
            elif n==cur_max:
                size+=1
            else:
                size=0
            res=max(res,size)
        return res
        
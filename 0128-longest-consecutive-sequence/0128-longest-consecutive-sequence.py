class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        res=0
        for num in nums:
            if (num -1) not in numSet:
                length=0
                while (num+length) in numSet:
                    length+=1
                res=max(res,length) 
        return res
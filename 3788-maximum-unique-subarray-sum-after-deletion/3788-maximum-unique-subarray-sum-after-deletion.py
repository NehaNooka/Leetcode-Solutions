class Solution:
    def maxSum(self, nums: List[int]) -> int:
        maxNum=max(nums)
        if maxNum<0: return maxNum
        numSet=set()
        for num in nums:
            if num >0 and num not in numSet:
                numSet.add(num)
        return sum(numSet)
        
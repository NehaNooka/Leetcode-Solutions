class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ans=[]
        xor=0
        for num in nums:
            xor^=num
        mask=(1<<maximumBit)-1
        for num in reversed(nums):
            ans.append(xor^mask)
            xor^=num
        return ans
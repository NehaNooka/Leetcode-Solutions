class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        parity = nums[0]%2
        odd = even = both = 0

        for n in nums:
            if n%2==0:
                even+=1
            else:
                odd+=1
            
            if n%2==parity:
                both+=1
                parity = 1-parity
        
        return max(odd, even, both)

        
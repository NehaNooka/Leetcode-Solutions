class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums)<k: return -1
        unique=set(nums)
        res = sum(1 if n > k else 0 for n in unique)
        return res


        
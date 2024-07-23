class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        nums.sort(key=lambda n:(c[n],-n))
        return nums

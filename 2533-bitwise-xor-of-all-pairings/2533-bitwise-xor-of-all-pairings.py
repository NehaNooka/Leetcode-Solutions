class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        if len(nums2)%2:
            for i in range(len(nums1)):
                ans = ans ^ nums1[i] 
        if len(nums1)%2:
            for i in range(len(nums2)):
                ans = ans ^ nums2[i]
        return ans
        



        
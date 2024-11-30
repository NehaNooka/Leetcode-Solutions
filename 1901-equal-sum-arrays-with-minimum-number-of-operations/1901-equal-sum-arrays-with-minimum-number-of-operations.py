class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if 6*len(nums1) < len(nums2) or 6*len(nums2) < len(nums1): return -1 # impossible 
        
        if sum(nums1) < sum(nums2): nums1, nums2 = nums2, nums1
        s1, s2 = sum(nums1), sum(nums2) # s1 >= s2
            
        nums1.sort()
        nums2.sort()
        
        ans = i = 0
        j = len(nums1)-1
        
        while s1 > s2: 
            if i >= len(nums2) or 0 <= j and nums1[j] - 1 > 6 - nums2[i]: 
                s1 += 1 - nums1[j]
                j -= 1
            else: 
                s2 += 6 - nums2[i]
                i += 1
            ans += 1
        return ans 

        
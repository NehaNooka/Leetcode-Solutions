class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_sum=sum(x if x!=0 else 1 for x in nums1)
        nums2_sum=sum(x if x!=0 else 1 for x in nums2)

        nums1_zeroes=nums1.count(0)
        nums2_zeroes=nums2.count(0)

        if (nums1_zeroes==0 and nums2_sum>nums1_sum) or (nums2_zeroes==0 and nums1_sum>nums2_sum):
            return -1
        return max(nums1_sum,nums2_sum)
        
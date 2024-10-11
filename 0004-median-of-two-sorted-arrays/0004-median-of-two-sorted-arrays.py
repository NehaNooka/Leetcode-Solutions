class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums.sort()

        if len(nums)%2==0:
            mid1=nums[len(nums)//2]
            mid2=nums[(len(nums)//2)-1]
            return (mid1+mid2)/2
        else:
            return nums[(len(nums)//2)]
        
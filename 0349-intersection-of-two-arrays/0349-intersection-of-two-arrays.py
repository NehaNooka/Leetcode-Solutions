class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set2=set(nums2)
        res=set()
        for e in nums1:
            if e in set2: res.add(e)
        return list(res)

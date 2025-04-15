from typing import List

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        numsMap = {v: k for k, v in enumerate(nums2)}  # Map nums2 values to their indices
        pos1 = [numsMap[v] for v in nums1]  # Convert nums1 to indices in nums2
        
        # Fenwick Tree helper functions
        def update(bit, idx, val):
            while idx < len(bit):
                bit[idx] += val
                idx += idx & -idx
        
        def query(bit, idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & -idx
            return s
        
        # Fenwick Tree for counting elements
        left_count = [0] * n
        bit = [0] * (n + 1)
        
        # Count elements to the left of each index
        for i in range(n):
            left_count[i] = query(bit, pos1[i])
            update(bit, pos1[i] + 1, 1)
        
        # Reset Fenwick Tree for counting elements to the right
        bit = [0] * (n + 1)
        res = 0
        
        # Count elements to the right of each index and calculate good triplets
        for i in range(n - 1, -1, -1):
            right_count = query(bit, n) - query(bit, pos1[i])
            res += left_count[i] * right_count
            update(bit, pos1[i] + 1, 1)
        
        return res

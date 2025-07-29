class Solution:
    def smallestSubarrays(self, nums):
        n = len(nums)
        nearest = [-1] * 32
        ans = [0] * n

        for i in range(n - 1, -1, -1):
            for j in range(32):
                if nums[i] & (1 << j):
                    nearest[j] = i

            lastSetBit = i
            for j in range(32):
                if nearest[j] != -1:
                    lastSetBit = max(lastSetBit, nearest[j])

            ans[i] = lastSetBit - i + 1

        return ans
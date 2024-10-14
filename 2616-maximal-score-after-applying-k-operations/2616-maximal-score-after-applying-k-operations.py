from math import ceil
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans=0
        new_num=[-x for x in nums]
        heapq.heapify(new_num)
        print(nums)
        while k:
            num=-heapq.heappop(new_num)
            ans+=num
            heapq.heappush(new_num, -ceil(num/3))
            k-=1
        return ans

        
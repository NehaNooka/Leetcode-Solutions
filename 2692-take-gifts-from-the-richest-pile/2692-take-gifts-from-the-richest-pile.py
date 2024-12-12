class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts=[-g for g in gifts]
        heapq.heapify(gifts)
        while k:
            max_gift=-1*heapq.heappop(gifts)
            heapq.heappush(gifts,-1*math.isqrt(max_gift))
            k-=1
        return -1*sum(gifts)

        
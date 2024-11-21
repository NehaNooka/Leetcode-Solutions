class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        l=prices[0]
        for r in prices[1:]:
            if r>l:
                profit=max(profit,r-l)
            else:
                l=min(l,r)
        return profit
        
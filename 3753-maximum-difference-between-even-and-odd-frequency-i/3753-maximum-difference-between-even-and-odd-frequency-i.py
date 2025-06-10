class Solution:
    def maxDifference(self, s: str) -> int:
        count=Counter(s)
        odd,even=0,float('inf')
        for v in count.values():
            if v%2: odd=max(odd,v)
            else: even=min(even,v)
        return odd-even
            

        
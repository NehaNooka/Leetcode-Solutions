class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors.extend(colors[:(k-1)])
        res=0
        l=0
        for r in range(len(colors)):
            if colors[r]==colors[r-1]:
                l=r
            if (r-l+1)>=k:
                res+=1
        return res
        
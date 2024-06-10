class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        s=0
        expected=sorted(heights)
        if heights==expected:
            return 0
        for i,j in zip(heights,expected):
            if i!=j:
                s+=1
        return s
        
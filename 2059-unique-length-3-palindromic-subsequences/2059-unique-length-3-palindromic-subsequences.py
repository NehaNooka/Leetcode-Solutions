class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res=set() #(outer,mid)
        left=set()
        right=Counter(s)

        for m in s:
            right[m]-=1
            for o in left:
                if right[o]>0:
                    res.add((o,m))
            left.add(m)
        return len(res)
        
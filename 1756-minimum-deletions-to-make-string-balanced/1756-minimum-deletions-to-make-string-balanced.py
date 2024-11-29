class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count_right,b_count_left=0,0
        for c in s:
            if c=='a': a_count_right+=1
        
        res=len(s)
        for c in s:
            if c=='a': a_count_right-=1
            res=min(res,b_count_left+a_count_right)
            if c=='b': b_count_left+=1
        return res
        
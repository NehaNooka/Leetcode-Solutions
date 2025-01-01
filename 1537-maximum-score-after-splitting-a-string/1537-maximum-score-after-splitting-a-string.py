class Solution:
    def maxScore(self, s: str) -> int:
        res,zeroes,ones=0,0,s.count('1')
        for i in range(len(s)-1):
            if s[i]=='0': zeroes+=1
            else: ones-=1
            res=max(res,zeroes+ones)
        return res


        
        
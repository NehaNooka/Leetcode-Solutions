class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ans=''
        for i in range(len(s)):
            ans+=str(ord(s[i])-ord('a') +1)
        
        for i in range(k):
            res=0
            for i in range(len(ans)):
                res+=int(ans[i])
            ans=str(res)
        return res


        
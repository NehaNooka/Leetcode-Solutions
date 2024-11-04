class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
        if not s: return 0
        i,sign=0,1
        if s[0]=='-':
            sign=-1
            i=1
        elif s[0]=='+':
            i=1
        ans=0
        for c in s[i:]:
            if not c.isdigit():
                break
            ans=ans*10+int(c)
        return max(min(ans*sign,2**31-1), -2**31)



        
class Solution:
    def reverse(self, x: int) -> int:
        flag=False
        if x<0:
            flag=True
            x=-x
        res=int(str(x)[::-1]) if int(str(x)[::-1]) < pow(2,31) else 0
        return res if flag==False or res==0 else -res
        
        
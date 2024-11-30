class Solution:
    def calculate(self, s: str) -> int:
        cur,res,stack,sign=0,0,[],1
        for c in s:
            if c.isdigit():
                cur=cur*10+int(c)

            elif c=='+' or c=='-':
                res+=cur*sign
                sign=1 if c=='+' else -1
                cur=0
            elif c=='(':
                stack.append((res,sign))
                res=0
                sign=1
            elif c==')':
                res+=cur*sign
                prev_num,prev_sign=stack.pop()
                res= prev_num + res*prev_sign
                cur=0
        res+=cur*sign
        return res

        
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1,num2=list(num1)[::-1], list(num2)[::-1]
        res=[]
        leng=max(len(num1),len(num2))
        i,carry=0,0
        while i<leng or carry>0:
            i1=num1[i] if i<len(num1) else 0
            i2=num2[i] if i<len(num2) else 0
            total=int(i1)+int(i2)+carry
            carry=total//10
            total=total%10
            res.append(str(total))
            i+=1
        return ''.join(res[::-1])
         
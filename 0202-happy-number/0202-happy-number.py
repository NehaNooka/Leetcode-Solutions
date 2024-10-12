class Solution:
    def isHappy(self, n: int) -> bool:
        visit=set()
        while n not in visit:
            visit.add(n)
            if n == 1: return True
            sum=0
            n=str(n)
            for i in range(len(n)):
                sum+=pow(int(n[i]),2)
            n=sum
        return False
        

        